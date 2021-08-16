#Preparação dos Dados para criar o .csv 

import pandas as pd
from pymongo import MongoClient

#criando uma variável com a credential do MONGODB
mongo_uri = 'insert your mongoDB credential'
conn = MongoClient(mongo_uri)
#Indicando qual a colletion irei acessar e colocando em uma variável conn
conn=conn['DataBaseName']
#buscando todos os tweets dessa collection e colocando em uma variável cursor
cursor = conn['CollectionName'].find()

df =  pd.DataFrame(list(cursor))


df_allmedicines_truncated_true = pd.DataFrame(list(conn.Twitter.find({'truncated':True},{"id_str":1,"extended_tweet.full_text": 1})))
df_allmedicines_truncated_true['text'] = df_allmedicines_truncated_true['extended_tweet'].apply(lambda cell: cell['full_text'])
df_allmedicines_truncated_true.drop('extended_tweet', 1, inplace=True)

df_allmedicines_truncated_false = pd.DataFrame(list(conn.Twitter.find({'truncated':False},{"id_str":1, "text": 2})))

frames = [df_allmedicines_truncated_false, df_allmedicines_truncated_true]
df_allmedicines = pd.concat(frames)
df_allmedicines = df_allmedicines.drop_duplicates(subset='id_str', keep = 'first')

'''
#Fazendo a limpeza dos Tweets: replacing links, usuários com @ por vazio
df_allmedicines_replace=df_allmedicines['text']
df_allmedicines_replace = df_allmedicines_replace.replace(
    to_replace=['http://\S+|https://\S+', '@\S+', ',', '!', '&', '#',],
    value='',
    inplace=True,
    regex=True
)

#Fazendo a limpeza dos Tweets 2: removendo acentos
df_allmedicines['text'] = df_allmedicines['text'].str.normalize('NFKD').str.encode('ascii','ignore').str.decode('utf-8')
'''

df_allmedicines_replace=df_allmedicines['text']
df_allmedicines_replace = df_allmedicines_replace.replace(
    to_replace=['\n'],
    value='',
    inplace=True, 
    regex=True
)


df_allmedicines.head(10000)


df_comid = df_allmedicines.iloc[0:3001]
df_comid.to_csv("3000TweetscomId.csv", index=False)
#df_allmedicines = df_allmedicines.filter(items=['text'])

df_semid = df_allmedicines.iloc[3000:5700]
#df_allmedicines.columns.values
df_semid.to_csv("3000TweetssemId2.csv", sep = ';', index=False, header=False, columns=['text'])