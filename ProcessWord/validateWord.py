from Pangrams import pangrams

wordScore = 0

def validateWord(wordIn):
    if len(wordIn) < 4:
        print("The word must contain at least 4 letters")
    else:
        scoreWord(wordIn)

def scoreWord(wordIn):
    wordScore = len(wordIn)
    if (pangrams.is_pangram(wordIn)):
        wordScore += 7
    return wordScore

