from Pangrams import pangrams
import json

wordScore = 0

def validateWord(wordIn):
    if len(wordIn) < 4:
        print("The word must contain at least 4 letters")
        return wordScore
    else:
        checkWordExists(wordIn)

def scoreWord(wordIn):
    wordScore = len(wordIn)
    if (pangrams.is_pangram(wordIn)):
        print("That is a panagram")
        wordScore += 7
    return wordScore

def checkWordExists(wordIn):
    with open("Pangrams/words_dictionary.json", "r") as words_file:
        word_dict = json.load(words_file)
        if wordIn in word_dict:
            scoreWord(wordIn)
        else:
            print("Word does not exist")
            return wordScore


