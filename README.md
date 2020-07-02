# System-To-Gauge-Public-reaction-to-TV-Shows
A system with appropriate data pipeline to Gauge and Report Public Reaction to Various TV Shows.

In this project we present a prototypical demonstration of how opinions from public social media platforms, such as tweets from twitter, can be used to drive business decisions, using various tools and technologies from the DW & BI domain. We’ve restricted our scope to only tweets related to two TV shows namely Money Heist and Tiger King of Netflix. Essentially, we extract key indicators from these tweets to drive business decisions with respect to future shows at Netflix. We first use the GetOldTweets3 library of python to extract tweets, we then manually insert these extracted and tabularized tweets into a RDBMS Table, defined inside the MySql Instance of the Google Cloud. We then use PySpark to load data into a Jupyter notebook and then perform some elementary descriptive analysis on the tweets. Further, we make use of TextBlob & NLTK libraries in python to classify the sentiments for each of the tweets. This system can be quite easily generalized for other products too apart from movies and TV Shows, only change would be the appropriate questions and metrics for the targeted product.

Use Case
Make use of publically available opinions to drive business insights such as below and many others.
1.	How different shows compare with one another?
2.	What are the sentiments with respect to a TV show?
3.	How people are reacting to announcements & trailers?
4.	What is the distribution of tweets pre-release and post-release with respect to a show?
5.	How does the distribution of different shows and seasons compare with one another?
6.	Is there a high demand for a particular type of Genre during a particular period?
7.	What are the most popular Genres?
8.	Does releasing 2 shows together benefit Netflix?
9.	Location specific insights for a show

Software Details
•	Data Extraction: Python library GetOldTweets3
•	Data Storage: MySQL database on Google Cloud
•	Data Processing and Basic Analysis: PySpark SQL and PySpark DataFrame
•	Advanced Analysis: Python libraries like Seaborn, NLTK, TextBlob

Demo: Click on the <a href="https://www.dropbox.com/l/scl/AABlkJDZQB74TbEP5KET37G_ddUCF9pKAIk">link</a> to view the demo video 

This was a group project involving

1. Mohammed Nifaullah Sailappai
2. Onkar Samant
3. Pravallika Mulukuri
4. Stephen Yeboah



