import view.gameUIs
from game_controller import gameManager, guessTemplate
import json
from Pangrams import pangrams
from view import gameUIs

Rankings = {1: "Meh!", 2: "Alright like!", 3: "Savage!", 4: "Massive!", 5: "Medazza!"}


class nytBee(gameManager, guessTemplate):

    def __init__(self):
        super().__init__()
        self.scores = []
        self.validWords = []
        self.totalscore = 0

        chosen_word = pangrams.getChosenWord()
        print(chosen_word)

    def process_word(self, chosen_word):
        chosen_set = set(chosen_word)
        for mid_letter in chosen_set:
            break
        print(mid_letter)

        while gameUIs != "exitgame":
            word_in = view.gameUIs.runningUI()
            if (len(word_in)) > 3:
                if mid_letter in word_in:
                    if self.validate_word(word_in):
                        result = self.scoreWord()
                        print("Score: ", result)
                        self.totalscore += result
                        self.scores.append(result)
                        self.validWords.append(word_in)
                else:
                    print("Word must contain the letter: ", mid_letter)
                    word_in = view.gameUIs.runningUI()
            else:
                print("Words must contain 4 letters")
                word_in = view.gameUIs.runningUI()

    def validate_word(self, word_in):
        with open("Pangrams/words_dictionary.json", "r") as words_file:
            word_dict = json.load(words_file)
            if word_in in word_dict:
                return True
            else:
                print("Word does not exist")
                return False

    def scoreWord(self, word_in):
        word_score = len(word_in)
        if pangrams.is_pangram(word_in):
            print("That is a pangram")
            word_score += 7
        return word_score

    def record_stats(self, word_score):
        pass
