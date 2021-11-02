from Pangrams import pangrams
import json

#These have been replaced with methods in the gameManager class
wordScore = 0

def validateWord(wordIn):
    if len(wordIn) < 4:
        print("The word must contain at least 4 letters")
        return False
    else:
        checkWordExists(wordIn)



def checkWordExists(wordIn):
    with open("Pangrams/words_dictionary.json", "r") as words_file:
        word_dict = json.load(words_file)
        if wordIn in word_dict:
            return True
        else:
            print("Word does not exist")
            return False


