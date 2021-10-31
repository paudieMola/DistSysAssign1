
def startingUI():
    start = input("Start New York Times Spelling Bee? y/n")
    print("To stop game type 'exitgame'")
    return start.lower()

def runningUI():
    guess = input("Enter word : ")
    return guess
