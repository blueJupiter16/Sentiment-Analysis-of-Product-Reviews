import pandas as pd
import gzip
import os
import string
import re

stop = [ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]

def touch_test(df, folder):
    for x in range(len(df.index[0:int(len(df)/2)])):
        filename = 'f' + folder + str(x) + '.txt'
        with open("test" + "/" + folder + "/" + filename, 'w') as output_file:
            output_file.write(''.join(df.reviewText[x]))

def touch_train(df, folder):
    for x in range(len(df.index[int(len(df)/2):])):
        filename = 'f' + folder + str(x) + '.txt'
        with open("training" + "/" + folder + "/" + filename, 'w') as output_file:
            output_file.write(''.join(df.reviewText[int(len(df)/2) + x]))

def make_folder(directory):
    folders = 5
    for i in range(folders):
        new_folder = str(i + 1)
        if not os.path.exists(directory + "/" + new_folder): os.makedirs(directory + "/" + new_folder)

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

def remove_stop(row):
    global stop
    lis=[word for word in row["reviewText"].split(" ") if word not in stop]
    string=""
    for word in lis:
        string=string+word+" "
    return string[0:len(string)-1]

df = getDF('reviews_Cell_Phones_and_Accessories_5.json.gz')
new = df[['overall','reviewText']].copy()
new['reviewText'] = new.apply(remove_stop,axis=1)

if not os.path.exists("test"): os.makedirs("test")
if not os.path.exists("training"): os.makedirs("training")

make_folder("test")
make_folder("training")

all_one = new[new['overall'] == 1]
all_one = all_one.reset_index();

all_two = new[new['overall'] == 2]
all_two = all_two.reset_index();

all_three = new[new['overall'] == 3]
all_three = all_three.reset_index();

all_four = new[new['overall'] == 4]
all_four = all_four.reset_index();

all_five = new[new['overall'] == 5]
all_five = all_five.reset_index();

touch_test(all_one, '1')
touch_test(all_two, '2')
touch_test(all_three, '3')
touch_test(all_four, '4')
touch_test(all_five, '5')

touch_train(all_one, '1')
touch_train(all_two, '2')
touch_train(all_three, '3')
touch_train(all_four, '4')
touch_train(all_five, '5')
