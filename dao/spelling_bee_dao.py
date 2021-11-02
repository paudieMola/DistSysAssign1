from tinydb import TinyDB
# not going to use to start from tinydb import Query

import random
import threading
import time


# create an instance of the Dao if none exists
# or use the instance if it has already been created.
# ensures only one instance of the game exists, and
# any threads accessing are locked when in use.

class SpellingBeeDao:
    __instance = None

    @staticmethod
    def get_instance():
        if SpellingBeeDao.__instance is None:
            with threading.Lock():
                if SpellingBeeDao.__instance is None:
                    SpellingBeeDao()
        return SpellingBeeDao.__instance

    def __init__(self):
        if SpellingBeeDao.__instance is not None:
            raise Exception("This is a singleton")
        else:
            SpellingBeeDao.__instance = self
#        self.db = TinyDB('gamesdb.json')
#        self.lock = threading.Lock()
 #       self.rand = random.random()

#    def add(self, bee):
#        self.lock.acquire()

        # just to simulate game operation
#        time.sleep(3)

        # beeQuery = Query() Maybe dont need if I'm not checking a condition
        # I'm not going to check a condition - just insert this game into the gamesdb
        # if not self.db.contains(Bee.chosenWord == bee.chosenWord):
        #self.db.insert({'gameType': bee.gametype, 'chosenWord': bee.chosenWord})

        #print('Insert attempted for '+bee.chosenWord+'  ' + str(self.rand))

#        self.lock.release()
