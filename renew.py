import os
import shutil


if(os.path.isfile("classifier_object.pkl")):
	os.remove("classifier_object.pkl")
if(os.path.isfile("test_data_bunch.pkl")):
	os.remove("test_data_bunch.pkl")
	
if(os.path.isfile("train_data_bunch.pkl")):
	os.remove("train_data_bunch.pkl")


shutil.rmtree('training')
shutil.rmtree('test')

os.system("extraction.py")
os.system("model.py")
