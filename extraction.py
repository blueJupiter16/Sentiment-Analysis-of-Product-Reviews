import pandas as pd
import gzip
import os

def touch(df, folder):
    for x in range(len(df.index)):
        filename = 'f' + str(x) + '.txt'
        with open(folder + "/" + filename, 'w') as output_file:
            output_file.write(df.reviewText[x])

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

folders = 5
for i in range(folders):
    new_folder = str(i+1)
    if not os.path.exists(new_folder): os.makedirs(new_folder)

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

touch(all_one, '1')
touch(all_two, '2')
touch(all_three, '3')
touch(all_four, '4')
touch(all_five, '5')