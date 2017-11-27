# Sentiment-Analysis-of-Product-Reviews

The Social network is a huge collection of opinions and reviews. Unlike reviews of E-Commerce websites, the reviews are unstructured and difficult to make sense of on a large-scale.

The goal of this project is to perform sentiment analysis on product reviews posted on social networking websites like twitter. The analysis will classify a particular post/review into a **5-Star** rating which can be used by companies to act upon a particular post or not.

The scope of this project is limited to analysis of review data for smartphones.



## Phases of the Project

1. Data collection and cleaning

   Customer review data is collected from an online source (http://jmcauley.ucsd.edu/data/amazon/) that contains data segregated into multiple categories. The data obtained from this source is in  JSON format which is parsed and cleaned according to the need of the model. 

   After cleaning, the data is separated into two parts: training set and testing set. The training set is used to train the ML model and the testing dataset is used for validation of the model and to calculate mathematical parameters. 

   ​

2. Model Building

   The project is a subdomain of Natural Language Processing. Sentiment analysis is a part of supervised machine learning algorithms where we use the data set and train the model. For this particular application, the algorithm used for classification is Support Vector Machines. 

   The model building phase uses python libraries for data analytics like scikit learn and pandas. 

   After training the and testing, following was observed: 

   ##### Precision: 0.8, F1- Score: 0.79, Accuracy: 78.9 %

   ​

3. Live streaming of Twitter Data
