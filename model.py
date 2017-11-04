from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics
import numpy as np

category = ['alt.atheism', 'soc.religion.christian','comp.graphics','sci.med']
twenty_train = fetch_20newsgroups(subset='train',categories=None,shuffle=True,random_state=42)
twenty_test = fetch_20newsgroups(subset='test',categories=None,shuffle=True,random_state=42)
docs_test = twenty_test.data
#print(twenty_train.target[:10])
#cout_vector = CountVectorizer()
#X_train = cout_vector.fit_transform(twenty_train.data)
#print(X_train.shape)
#print(cout_vector.vocabulary_.get(''))

#tfidf_transformer = TfidfTransformer()
#X_train_tfidf = tfidf_transformer.fit_transform(X_train)
#print(X_train_tfidf.shape)

#clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier())])#loss="hinge",penalty='l2',alpha=0.0001,random_state=None,max_iter=None,tol=None))])
text_clf.fit(twenty_train.data,twenty_train.target)

predicted = text_clf.predict(docs_test)
print(np.mean(predicted == twenty_test.target) * 100 ,"%")
print(metrics.classification_report(twenty_test.target,predicted,target_names=twenty_test.target_names))
"""s = "yes"
while(s != "No"):

    s = input()
    docs_new = []
    docs_new.append(s)
    #X_new_counts = cout_vector.transform(docs_new)
    #X_new_tfidf = tfidf_transformer.transform(X_new_counts)

    predicted = text_clf.predict(docs_new)

    for doc, category in zip(docs_new, predicted):
        print('%r => %s' % (doc, twenty_train.target_names[category]))"""
