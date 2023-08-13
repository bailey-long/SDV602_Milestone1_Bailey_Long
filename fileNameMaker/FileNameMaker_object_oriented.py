"""
FileNameMaker

Creates file names
"""
import csv
import random

class FileNameMaker:
    def __init__(self):
        self._action_verbs = []
        self._archaic_words = []
        self._weird_words = []
        self._file_name = ''
        self._load_word_lists()
        
    
    # Makes a file name by selecting a random word from each of three lists, 
    # each word is then concatenated to make a file name.

    # Read three lists of words from three csv files.
    # action_verbs.csv, archaic_words.csv and weird_words.csv.
    def _get_word_list(self,pFileName):
        word_list = []
        with open(pFileName) as csvfile:
            word_reader = csv.reader(csvfile)
            for row in word_reader:
                word_list += row
        return word_list
    
    def _load_word_lists(self):
        # get word lists
        self._action_verbs = self._get_word_list('action_verbs.csv')
        self._archaic_words = self._get_word_list('archaic_words.csv')
        self._weird_words = self._get_word_list('weird_words.csv')

    def _make_file_name(self):
        # make the file_name       
        self._file_name = self._weird_words[random.randint(0,len(self._weird_words)-1)]
        self._file_name += self._archaic_words[random.randint(0,len(self._archaic_words)-1)]
        self._file_name += self._action_verbs[random.randint(0,len(self._action_verbs)-1)]
   
    def get_name(self):
        self._make_file_name()
        return self._file_name
        
        
        
        


if __name__ == "__main__":
   # OO lets you create an Object that has resposibilty for ...
   file_namer_a = FileNameMaker() # as many instances as needed
   file_namer_b = FileNameMaker()
   
   print(file_namer_a.get_name())
   print(file_namer_b.get_name())