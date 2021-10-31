from Pangrams import pangrams
import json

def scoreWord(wordIn):
    wordScore = len(wordIn)
    if (pangrams.is_pangram(wordIn)):
        print("That is a panagram")
        wordScore += 7
    return wordScore