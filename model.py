from sklearn.datasets import fetch_20newsgroups
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn import metrics
import numpy as np
import _pickle as cPickle


train_data = load_files('training',description="Training Data",categories=None,load_content=True,shuffle=True,encoding=None,decode_error='strict',random_state=0)
#train_data = fetch_20newsgroups(subset='train',categories=None,shuffle=True,random_state=42)

##save bunch object
with open('train_data_bunch.pkl','wb') as fd:
    cPickle.dump(train_data,fd)

test_data = load_files('test',description="Training Data",categories=None,load_content=True,shuffle=True,encoding=None,decode_error='strict',random_state=0)
docs_test = test_data.data

##save bunch object
with open('test_data_bunch.pkl','wb') as fd:
    cPickle.dump(train_data,fd)


#print(train_data.target[:10])
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
                     ('clf', SGDClassifier())])
text_clf.fit(train_data.data,train_data.target)

##save classifier object
with open('classifier_object.pkl', 'wb') as fid:
    cPickle.dump(text_clf, fid)


'''s = "yes"
while(s != "No"):

    s = input()
    docs_new = []
    docs_new.append(s)
    predicted = text_clf.predict(docs_new)

    for doc, category in zip(docs_new, predicted):
        print('%r => %s' % (doc, train_data.target_names[category]))'''




def printPerformance(text_clf,test_data,docs_test):
    
    predicted = text_clf.predict(docs_test)
    print(np.mean(predicted == test_data.target) * 100 ,"%")
    print(metrics.classification_report(test_data.target,predicted,target_names=test_data.target_names))
