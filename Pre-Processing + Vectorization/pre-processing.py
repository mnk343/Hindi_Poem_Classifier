import csv
import pickle

from inltk.inltk import setup

setup("hi")
#This will give runtime error; check if it displays "done", if not run again after some time.

"""# Pre-processing"""

from inltk.inltk import tokenize

poems_data_path = './poems_data_merged.csv'
# 3 files for stopwords, decide later which one gives better results
stop_words_path = './Stopwords/stopwords1.txt'

poems_data = open(poems_data_path,'r')
stop_words_file = open(stop_words_path,'r')

reader = csv.reader(poems_data, delimiter=',')

stop_words = []
for stop_word in stop_words_file:
	stop_words.append(stop_word)

line_count = 0

all_data = []

for row in reader:
	if (line_count == 0):
		pass
	else:
		tokenized_poem = tokenize(row[4],'hi')
		filtered_poem = [word for word in tokenized_poem if not word in stop_words] 
		all_data.append([row[0],row[1],row[2],row[3],filtered_poem])
	line_count += 1

# for i in range (5) :
# 	print(all_data[i])

with open('processed_data.txt', 'wb') as processed_data:
   pickle.dump(all_data, processed_data)
