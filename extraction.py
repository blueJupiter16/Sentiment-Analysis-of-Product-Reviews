import pandas as pd
import gzip
import os

#number of reviews

num_reviews = 2000
num_test = 6000

def touch_test(df, folder):
    for x in range(len(df.index[num_reviews+1:num_reviews+num_test])):
		
        filename = 'f' + folder + str(x) + '.txt'
        with open("test" + "/" + folder + "/" + filename, 'w') as output_file:
            output_file.write(df.reviewText[x])

def touch_train(df, folder):
    for x in range(len(df.index[0:num_reviews])):
        filename = 'f' + folder + str(x) + '.txt'
        with open("training" + "/" + folder + "/" + filename, 'w') as output_file:
            output_file.write(df.reviewText[x])#int(len(df)/2) +

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

df = getDF('reviews_Cell_Phones_and_Accessories_5.json.gz')
new = df[['overall','reviewText']].copy()

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
