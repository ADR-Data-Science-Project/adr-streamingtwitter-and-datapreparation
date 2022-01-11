# Streaming Twitter and Data Preparation

<p>In this project, we built a dataset of Adverse Reactions to Antidepressant Drugs, using the Twitter API to obtain this data in real time.

With access granted, we used the Python libraries to perform queries and collect tweets, the main one used in this step was Tweepy.
</p>
<p>
We use a filter in the script with antidepressant keywords in 5 different classes (chemical and commercial name)
Searches in common formats on the social network, that is, using the drug “Fluoxetine”, we look for variations such as: @Fluoxetine, #Fluoxetine, Fluoxetine. In addition to ensuring the filtering of tweets by language in “pt” (Portuguese). <br>
</p>
<p>
The streaming script ran non-stop using an EC2 Linux instance on AWS of type t2.micro, a high availability cluster. Tweet collection started on 04/14/2021 and continues to happen until now.
</p>
<p>
Data were collected and stored in JSON format in a NoSQL database, more specifically, MongoDB, using the Pymongo library.
</p>
<a href="https://developer.twitter.com/en/docs/twitter-api" target="_blank"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" target="_blank"></a> <a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" target="_blank"></a> <a href="https://code.visualstudio.com/" target="_blank"><img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" target="_blank"></a> <a href="https://aws.amazon.com/pt" target="_blank"><img src="https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" target="_blank"></a></a> <a href="https://www.mongodb.com/pt-br" target="_blank"><img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white" target="_blank"></a>



#
This is part 1 of 5 of the course completion work. Developed by <a href="https://github.com/bpaixao">Beatriz Paixão</a> and <a href="https://github.com/katheleen-gregorato">Katheleen Gregorato</a>. See our publication in CONICT - IFSP at: https://bit.ly/3IsqULo
