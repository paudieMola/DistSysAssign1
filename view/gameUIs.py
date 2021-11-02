
def startingUI():
    start = (input("Start New York Times Spelling Bee? y/n")).lower
    print("To stop game type 'exitgame'")
    if start == "y":
        runningUI()
    else:
        exit()

def runningUI():
    guess = (input("Enter word (type 'exitgame' to stop) : ")).lower
    return guess
