from dao import spelling_bee_dao
import bee
from Pangrams import pangrams
from ProcessWord import validateWord

import threading

class AddThread(threading.Thread):
    def __init__(self, thread_id, name, bee):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.bee = bee
        self.dao = spelling_bee_dao.SpellingBeeDao.get_instance()

    def run(self):
        print("Starting " + self.name)
        self.dao.add(self.bee)
        print("Exiting " + self.name)

#must be put into a suitable module for player interaction
bee1 = bee.Bee('NYTbee', (pangrams.getChosenWord()))

print(validateWord.validateWord(bee1.chosenWord))

thread1 = AddThread(1, "Thread1", bee1)

thread1.start()

print("Exiting main thread")