"""
FileNameMaker

Creates file names
"""
import csv
import random

# Makes a file name by selecting a random word from each of three lists, 
# each word is then concatenated to make a file name.

# Read three lists of words from three csv files.
# action_verbs.csv, archaic_words.csv and weird_words.csv.
action_verbs = []
with open('action_verbs.csv') as csvfile:
    word_reader = csv.reader(csvfile)
    for row in word_reader:
        action_verbs += row
        
archaic_words = []
with open('archaic_words.csv') as csvfile:
    word_reader = csv.reader(csvfile)
    for row in word_reader:
       archaic_words += row
       
weird_words = []
with open('weird_words.csv') as csvfile:
    word_reader = csv.reader(csvfile)
    for row in word_reader:
       weird_words += row
       
file_name = weird_words[random.randint(0,len(weird_words)-1)]
file_name += archaic_words[random.randint(0,len(archaic_words)-1)]
file_name += action_verbs[random.randint(0,len(action_verbs)-1)]

print(file_name)
    


if __name__ == "__main__":
   pass