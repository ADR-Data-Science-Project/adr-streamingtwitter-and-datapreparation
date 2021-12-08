# Streaming Twitter and Data Preparation

<p>In this project, to build a dataset with Adverse Reactions to Medicines, we used the Twitter API for the data collection step, to obtain these data in real time. To use it, it is necessary to provide information about the purpose of its use, and once this is done, it is essential to create an application in the developer login, where the access keys and tokens (Consumer Key (API Key), Consumer Secret (API Secret) will be displayed , Access Token, Access Token Secret). 
<br>
With the access granted, Python libraries were used to perform queries and collections of tweets, the main one used in this stage was Tweepy, one of the functions being the collection of tweets.
</p>
<p>
To specify drug searches, a filter was developed that searches for tweets based on certain keywords, in this case, antidepressants from 5 different classes. In total there were 33 antidepressants and in addition to the chemical name, commercial names were added, totaling 50 keywords. Searches were made in a variety of formats common on the social network, that is, using the drug "Fluoxetina", for example, we searched for three variations such as: @Fluoxetina, #Fluoxetina, Fluoxetina. In addition, we guarantee the filtering of tweets by the language in “pt” (Portuguese). All the script for this step was developed in Visual Studio Code using the Python language. <br>
</p>
<p>
However, to collect and retain a large amount of data it was necessary for the streaming script to run uninterrupted. Therefore, we use a Linux instance of EC2 on AWS of type t2.micro, so all the collection and storage code was executed in the background through this virtual machine. The collection of tweets started on 14/04/2021 and continues to happen until now.
</p>
<p>
Data were collected and stored in JSON format in a NoSQL database, more specifically, MongoDB, using the Pymongo library.
</p>
<a href="https://developer.twitter.com/en/docs/twitter-api" target="_blank"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" target="_blank"></a> <a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" target="_blank"></a> <a href="https://code.visualstudio.com/" target="_blank"><img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" target="_blank"></a> <a href="https://aws.amazon.com/pt" target="_blank"><img src="https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" target="_blank"></a></a> <a href="https://www.mongodb.com/pt-br" target="_blank"><img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" target="_blank"></a>



#
This is part 1 of 5 of the course completion work. Developed by <a href="https://github.com/bpaixao">Beatriz Paixão</a> and <a href="https://github.com/katheleen-gregorato">Katheleen Gregorato</a>. See our publication in CONICT - IFSP at: https://bit.ly/3IsqULo
