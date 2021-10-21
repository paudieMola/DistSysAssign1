
#gametype can be expanded for other word games
class Bee:
    def __init__(self, gametype, chosenWord):
        self.gametype = gametype
        self.chosenWord = chosenWord
        self.players = []
        self.totalScore = 0
        self.submittedWords = []
        #just for debug take out when game is working
        print(chosenWord)

    #placeholder for when more developed
    def register_player(self, userName):
        return

