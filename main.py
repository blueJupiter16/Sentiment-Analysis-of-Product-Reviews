import _pickle as cPickle
from sklearn import metrics
import numpy as np


def printPerformance(text_clf,test_data,train_data):
    
    docs_test = train_data.data
    predicted = text_clf.predict(docs_test)
    print(np.mean(predicted == test_data.target) * 100 ,"%")
    print(metrics.classification_report(test_data.target,predicted,target_names=test_data.target_names))


def main():

    with open('classifier_object.pkl', 'rb') as fid:
        text_clf = cPickle.load(fid)

    with open('test_data_bunch.pkl', 'rb') as fid:
        test_data = cPickle.load(fid)

    with open('train_data_bunch.pkl', 'rb') as fid:
        train_data = cPickle.load(fid)

    #print(train_data.target_names)
    printPerformance(text_clf,test_data,train_data)



    s = "yes"
    while(s != "No"):

        s = input()
        docs_new = []
        docs_new.append(s)
        #X_new_counts = cout_vector.transform(docs_new)
        #X_new_tfidf = tfidf_transformer.transform(X_new_counts)

        predicted = text_clf.predict(docs_new)

        for doc, category in zip(docs_new, predicted):
            print('%r => %s' % (doc, test_data.target_names[category]))


##--------------Main


main()
