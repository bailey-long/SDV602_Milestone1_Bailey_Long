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
def get_word_list(pFileName):
    word_list = []
    with open(pFileName) as csvfile:
        word_reader = csv.reader(csvfile)
        for row in word_reader:
            word_list += row
    return word_list

# get word lists
action_verbs = get_word_list('action_verbs.csv')
archaic_words = get_word_list('archaic_words.csv')
weird_words = get_word_list('weird_words.csv')

# make the file_name       
file_name = weird_words[random.randint(0,len(weird_words)-1)]
file_name += archaic_words[random.randint(0,len(archaic_words)-1)]
file_name += action_verbs[random.randint(0,len(action_verbs)-1)]

print(file_name)
    


if __name__ == "__main__":
   pass