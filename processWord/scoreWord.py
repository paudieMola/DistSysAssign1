from Pangrams import pangrams
import json

##these have been replaced with methods in the gameManager class
def scoreWord(wordIn):
    wordScore = len(wordIn)
    if (pangrams.is_pangram(wordIn)):
        print("That is a panagram")
        wordScore += 7
    return wordScore