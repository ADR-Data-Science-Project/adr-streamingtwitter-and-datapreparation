import json
import pymongo
import tweepy
import sys
import yaml

#Imprimir na tela os argumentos enviados pela linha de comando
print(sys.stderr, 'Application: ', sys.argv[0])
print(sys.stderr, 'Database: ', sys.argv[1])
print(sys.stderr, 'Collection: ', sys.argv[2])
print(sys.stderr, 'YAML file: ', sys.argv[3])
print(sys.stderr, 'Keywords: ', sys.argv[4])
print(sys.stderr, 'Keywords (ID): ', sys.argv[5])

try:
    with open(sys.argv[3]) as file:
        # Carregar o arquivo medicineskeywords.yaml
        # Ele possui os termos que serão buscados no Twitter
        # Ele possui o ID das contas que serão rastreadas no Twitter
        medicines_list = yaml.load(file, Loader=yaml.FullLoader)    

    # Imprimir na tela os termos e IDs do arquivo medicineskeywords.yaml
    print(sys.stderr, 'Termos dos Medicamentos: ', medicines_list[sys.argv[4]])
    print(sys.stderr, 'IDs dos Medicamentos: ', medicines_list[sys.argv[5]])

    #Credentials do twitter inseridas em um arquivo
    # Códigos de acesso ao Twitter

    with open(sys.argv[6], 'r') as twcred:
        consumer_key = twcred.readline().strip('\n')
        consumer_secret = twcred.readline().strip('\n')
        access_key = twcred.readline().strip('\n')
        access_secret = twcred.readline().strip('\n')


    # Criar a instância do objeto da biblioteca tweepy.
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)


    class CustomStreamListener(tweepy.StreamListener):
        """
        tweepy.StreamListener é a classe da biblioteca tweepy utilizada para acessar o Twitter 
        Streaming API. Permitirá coletar tweets em tempo real.
        """
        def __init__(self, api):
            self.api = api
            super(tweepy.StreamListener, self).__init__()
            
            #Conexão com o MongoDB
            uri = "mongoDBcredential"
            self.db = pymongo.MongoClient(uri).get_database(sys.argv[1])
            
        def on_data(self, tweet):
            '''
            Será acionado todas as vezes que um stream de dados for recebido (tweets) e armazenará no MongoDB        
            '''       
            tweet=json.loads(tweet)

            #if para retirar os retweets sem comentários
            #count=self.db.get_collection(sys.argv[2]).count_documents(tweet.retweeted)
            if 'RT @' not in tweet['text']:
                self.db.get_collection(sys.argv[2]).insert_one(tweet)

            else:
                pass
            return True 

        def on_error(self, status_code):
            # Será acionado quando houver erro
            print(sys.stderr, 'Encontrou erro com código:', status_code)
            return True # Não encerrará o processo de stream

        def on_timeout(self):
            # Será acionado caso ocorra timeout
            print(sys.stderr, 'Timeout.....')
            return True # Não encerrará o processo de stream

    print(sys.stderr, 'Stream rodando')
    # Criar objeto stream
    sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
    #Definirá os parâmetros de busca.
    sapi.filter(track=medicines_list[sys.argv[4]], languages=["pt"])
