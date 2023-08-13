"""
FileNameMaker

Creates file names
"""
import csv
import random
import numpy
import matplotlib  

# Makes a file name by selecting a random word from each of three lists, 
# each word is then concatenated to make a file name.

# Read three lists of words from three csv files.
# action_verbs.csv, archaic_words.csv and weird_words.csv.
def get_words(aFileName):
    words = []
    with open(aFileName) as csvfile:
        word_reader = csv.reader(csvfile)
        for row in word_reader:
            words += row
    return words
        
word = lambda x : get_words(x)[random.randint(0,len(get_words(x))-1)]
        

print(
      word('weird_words.csv')   +  \
      word('archaic_words.csv') + \
      word('action_verbs.csv')
    ) 



if __name__ == "__main__":
   pass