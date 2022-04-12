import time
class RPGInfo():
    
    def __init__(self, game_title):
        self.title = game_title
    
    def welcome(self):
        print("************************************")
        print("** Welcome to The Baker Incident! **")
        print("************************************")
        print("")
        time.sleep(2)
        print("In " + self.title + " you play as a detective hired to investigate the mysterious disappearance of Henry Baker, an eccentric millionaire.")
        print("")
        time.sleep(2)
        print("Explore Mr. Baker's mansion, talk to its occupants, and search for clues to find out where he went (or perhaps, who took him?).")
        print("")

    @staticmethod
    def info():
        print("Version 1.1, published 4/11/2022")

    @classmethod
    def credits(cls):
        print("Thank you for playing!")
        print("")
        time.sleep(1)
        print("Created by Brennan League")
        print("")
        print("*************************")
        print("")
        time.sleep(1)
        print("Additional thanks to:")
        time.sleep(1)
        print("~The Stoned Woofer, for their words of encouragement, help with playtesting, and for owning the weirdest cat I've ever heard.")
        time.sleep(1)
        print("~Smudge, for their words of encouragement, and the final piece of the story's puzzle, the art supplies.")
        time.sleep(1)
        print("~Jess, for keeping me in line, and for allowing me to use her goofy dog as an NPC.")
        time.sleep(1)
        print("~Paris, for help with playtesting.")
        time.sleep(1)
        print("~Marc, for help with playtesting.")
        time.sleep(1)
        print("~JJ, for additional character ideas.")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        print("If you found a bug, or would like to provide feedback, please contact: Gnome at Home#0974 on Discord")
        time.sleep(10)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("To anyone who wants to edit this code for future use (myself included), I am deeply, deeply sorry.")