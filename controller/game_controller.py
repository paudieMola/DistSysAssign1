from abc import ABC, abstractmethod

class gameManager(ABC):
    def __init__(self):
        self.game = None

    def set_game(self, game):
        self.game = game
        #initialize the different fields for different games
        self.post_init()

    def end_game(self):
        #is here where i need to return final score?
        self.game.active = False

    @abstractmethod
    # has to be overridden
    def post_init(self):
        pass

#the template for processing and scoring each guess in a game
class guessTemplate(ABC):
    def process_guess(self, guessedWord):
       # here if the guessedWord is "exitgame" the game will end
        #if guessedWord == "exitgame"
            #result = self.getFinalScore()
        #result = self.scoreWord(guessedWord)
        #self.record_stats(result) I'll see if this is really needed
        pass

    @abstractmethod
    #put in player index after multiple players added
    def validate_word(self, word_In):
        pass

    @abstractmethod
    def scoreWord(self, word_In):
        pass

#    @abstractmethod
#    def getFinalScore(self):
#        pass

#    @abstractmethod
#    def getRankings(self):
#        pass

#    @abstractmethod
#   def record_stats(self, result):
#        pass
