from room import Room
from item import Item
from character import Character
from rpginfo import RPGInfo
from random import randint
import time

baker_incident = RPGInfo("The Baker Incident")
baker_incident.welcome()
RPGInfo.info()
backpack = []

print("")
time.sleep(5)
print("Please enter your name: ")
player_name = input("> ")


#create various rooms
front_yard = Room("Front Yard")
front_yard.set_description("An overgrown yard full of weeds. A white pitbull with a brown spot over one ear rapidly dashes back and forth through the grass.")

foyer = Room("Foyer")
foyer.set_description("The sun peeking in through the foyer's skylight illuminates dust motes floating in the air. An older man in nice clothing is standing stiffly by the doorway.")

great_hall = Room("Great Hall")
great_hall.set_description("A grand hallway with lots of furniture and decorations, all of which are covered by sheets.")

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room("Ballroom")
ballroom.set_description("This room feels not unlike a nice pair of genie pants")

banquet_hall = Room("Banquet Hall")
banquet_hall.set_description("A room containing a large banquet table and fancy place settings, all covered in dust")

pantry = Room("Pantry")
pantry.set_description("A cramped, musty room filled with dry goods.")

library = Room("Library")
library.set_description("An extravagant personal library with packed bookshelves covering each wall.")

study = Room("Study")
study.set_description("A modest study with a mahogany desk with a reading lamp on top. Behind the desk, a muscular, bearded man sits in a high-backed leather chair.")

downstairs_hallway = Room("Downstairs Hallway")
downstairs_hallway.set_description("It's a hallway that is downstairs.")

sunroom = Room("Sunroom")
sunroom.set_description("A glass room filled with many plants and wicker furniture. A young man sits in a wicker chair, fidgeting nervously.")

upstairs_hallway = Room("Upstairs Hallway")
upstairs_hallway.set_description("To the north is a door with a dark, narrow stairway leading upwards. You'll need a light to safely climb the stairs.")

master_bedroom = Room("Master Bedroom")
master_bedroom.set_description("A king-sized four poster bed stands centered along the far wall, with identical dressers on either side of it.")

master_bathroom = Room("Master Bathroom")
master_bathroom.set_description("A large jacuzzi tub with mineral rings sits below a window overlooking the street. A double vanity stands adjacent to it. One of the faucets drips occasionally.")

guest_bedroom = Room("Guest Bedroom")
guest_bedroom.set_description("A small bedroom filled with dusty boxes. It looks like it became a \"catch-all\" room after lack of use. A beautiful woman is rummaging through the boxes with a scowl on her face.")

guest_bathroom = Room("Guest Bathroom")
guest_bathroom.set_description("A disgusting bathroom that might've seen better days, but from its current state, it's hard to say when.")

attic = Room("Attic")
attic.set_description("The light from the lantern illuminates your passage up the creaky, narrow stairwell leading up into the attic. The attic is filled with a plethora of canvases covered with strange sigils and runes. The bottom of each canvas is signed, \"Smudge\"")

secret_room = Room("Secret Room")
secret_room.set_description("The bookshelf swings open to reveal a secret room with various photos and documents pinned along the walls, with a small desk buried in one corner. A notebook lies open on the desk, its pages filled with messy notes about magic and shapeshifting.")

room_list = [front_yard, foyer, study, great_hall, kitchen, ballroom, banquet_hall, pantry, library, downstairs_hallway, upstairs_hallway, master_bedroom, master_bathroom, guest_bathroom, guest_bedroom, sunroom, attic, secret_room]

#linking rooms together
front_yard.link_room(foyer, "north")

foyer.link_room(great_hall, "north")
foyer.link_room(study, "east")
foyer.link_room(front_yard, "south")
foyer.link_room(banquet_hall, "west")

great_hall.link_room(downstairs_hallway, "north")
great_hall.link_room(library, "east")
great_hall.link_room(foyer, "south")
great_hall.link_room(kitchen, "west")

kitchen.link_room(great_hall, "east")
kitchen.link_room(banquet_hall, "south")
kitchen.link_room(pantry, "west")

ballroom.link_room(banquet_hall, "north")

banquet_hall.link_room(kitchen, "north")
banquet_hall.link_room(foyer, "east")
banquet_hall.link_room(ballroom, "south")

pantry.link_room(kitchen, "east")


library.link_room(study, "south")
library.link_room(great_hall, "west")

study.link_room(library, "north")
study.link_room(foyer, "west")

secret_room.link_room(library, "west")

downstairs_hallway.link_room(sunroom, "north")
downstairs_hallway.link_room(upstairs_hallway, "east")
downstairs_hallway.link_room(great_hall, "south")
downstairs_hallway.link_room(upstairs_hallway, "west")

sunroom.link_room(downstairs_hallway, "south")

upstairs_hallway.link_room(guest_bedroom, "east")
upstairs_hallway.link_room(downstairs_hallway, "south")
upstairs_hallway.link_room(master_bedroom, "west")

master_bedroom.link_room(master_bathroom, "north")
master_bedroom.link_room(upstairs_hallway, "east")

master_bathroom.link_room(master_bedroom, "south")

guest_bedroom.link_room(guest_bathroom, "north")
guest_bedroom.link_room(upstairs_hallway, "west")

guest_bathroom.link_room(guest_bedroom, "south")

attic.link_room(upstairs_hallway, "south")


#create various items

dog_treats = Item("dog treats")
dog_treats.set_description("A small bag of bone-shaped dog treats")

revealing_letter = Item("revealing letter")
revealing_letter.set_description("A letter from Henry Baker which indicates he thought he was being followed, and he was concerned for his safety.")

buffalo_wings = Item("buffalo wings")
buffalo_wings.set_description("A basket of buffalo wings. They're still warm...")

transfiguration_book = Item("transfiguration book")
transfiguration_book.set_description("A thick, leather-bound tome with the title \'A Beginner's Guide to Transfiguration\' etched on the cover in gold-leaf.")

matchbook = Item("matchbook")
matchbook.set_description("A book of matches with a striking strip.")

lantern = Item("lantern")
lantern.set_description("An unlit oil lantern.")

art_supplies = Item("art supplies")
art_supplies.set_description("An assortment of unlabled art supplies, which radiate a strange energy.")


#create various characters

hermes = Character("Hermes", "A friendly pitbull")
hermes.set_conversation_0("\"Woof!\"")
hermes.set_soft_spot("dog treats")
hermes.set_conversation_1("*pants contentedly*")

eugene = Character("Eugene Baker", "A nervous-looking young man")
eugene.set_conversation_0("\"I- I'm Henry Baker's s-son, I j-just want t-t-to know wh-what happened to m-m-my f-father!\"")
eugene.set_soft_spot("revealing letter")
eugene.set_conversation_1("\"Th-thank you so much! T-talk to M-Mister Bruce, I-I'll let him know to h-help you any way he c-can!\"")

jj = Character("JJ", "A muscular, bearded man. He looks hungry.")
jj.set_conversation_0("\"Hey kid, you wanna arm wrestle?\"")
jj.set_soft_spot("buffalo wings")
jj.set_conversation_1("\"Oh, those look good! Alright, I'll let you off this time, but once I'm done eating, we're gonna arm wrestle for sure!\" JJ walks away, already digging in to the basket of wings.")

widget = Character("Widget", "A strange black cat with a white dress collar and a black bowtie. He looks to be missing a tail.")
widget.set_conversation_0("The cat meows at you with an almost human-sounding, \"Hello?\"")

wayne_bruce = Character("Wayne Bruce", "A balding man dressed in a vest and slacks. He is Henry Baker's butler.")
wayne_bruce.set_conversation_0("*Wayne eyes you disdainfully*")
wayne_bruce.set_conversation_1("\"Have you read \'A Beginner's Guide to Transfiguration\'? It's quite good, Master Baker has a copy in his library if you'd like to borrow it.\"")

hermes_and_widget = Character("Hermes and Widget", "Hermes stands over Widget, who's cowering in the corner of the room. Hermes lets out a low growl as you enter.")

#place various items
front_yard.set_item(revealing_letter)
pantry.set_item(dog_treats)
banquet_hall.set_item(buffalo_wings)
secret_room.set_item(lantern)
attic.set_item(art_supplies)

#place various characters
front_yard.set_character(hermes)
foyer.set_character(wayne_bruce)
study.set_character(jj)
sunroom.set_character(eugene)


#establish starting room and status

widget_room = randint(3, 13)
room_list[widget_room].set_character(widget)
current_room = front_yard
dead = False

while dead == False:
    time.sleep(1)
    print("")
    current_room.details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()

    if inhabitant is not None:
        print("")
        inhabitant.describe()
    if item is not None:
        print("")
        item.describe()

    if current_room != room_list[widget_room]:
        meow_chance = randint(1, 10)
        if meow_chance == 10:
            print("")
            print("You hear an odd voice say, \"Hello?\" from somewhere in the house.")
    
    print("")
    current_room.adjacent()

    print("")
    print("What do you do? (type \'help\' for a list of commands)")
    command = input("> ")
    time.sleep(1)

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
        if hermes.affinity == 0:
            room_list[widget_room].set_character(None)
            widget_room = randint(3, 13)
            room_list[widget_room].set_character(widget)
    
    elif command == "talk":
        if inhabitant is not None:
            if inhabitant.conversation_0 is not None:
                inhabitant.talk()
            else:
                print("They don't want to talk to you.")
        else:
            print("Only a madman talks to themselves")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack.")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing to take in this room.")

    elif command == "backpack":
        print(backpack)

    elif command == "give":
        print("What do you offer " + inhabitant.name + "?")
        gift_item = input("> ")
        if gift_item in backpack:
            if inhabitant.give_gift(gift_item) == True:
                backpack.remove(gift_item)
        else:
            print("You don't have a " + gift_item)

        
    elif command == "help":
        print("LIST OF COMMANDS:")
        print("~north, south, east, west: used to navigate between areas.")
        print("~talk: hear what an NPC has to say.")
        print("~take: add an item to your backpack.")
        print("~give: offer an item to an NPC as a gift. If they like it, they might help you in some way!")
        print("~backpack: list all items currently in your backpack.")
        print("")
        print("If you discover any bugs or would like to provide feedback, please contact: Gnome at Home#0974 on Discord")
    
    if eugene.affinity == 1:
        wayne_bruce.affinity = 1
    if jj.affinity == 1:
        study.set_character(None)
    if study.character == None:
        study.set_item(matchbook)
        study.set_description("A modest study with a mahogany desk with a reading lamp on top. Behind the desk is a high-backed leather chair.")
    if "matchbook" in backpack:
        study.set_item(None)
    if wayne_bruce.affinity == 1:
        library.set_item(transfiguration_book)
    if "lantern" in backpack and "matchbook" in backpack:
        upstairs_hallway.link_room(attic, "north")
    if "transfiguration book" in backpack:    
        library.link_room(secret_room, "east")
        library.set_item(None)
        library.set_description("An extravagant personal library with packed bookshelves covering each wall. One of the bookshelves has swung open to reveal a secret room.")
    if guest_bedroom.character == None:
        guest_bedroom.set_description("A small bedroom filled with dusty boxes. It looks like it became a \"catch-all\" room after lack of use.")
    if hermes.affinity == 1 and front_yard.get_character() != None:
        print("Without warning, Hermes takes off like a bullet into the house. Strange...")
        front_yard.set_character(None)
        room_list[widget_room].set_character(None)
        room_list[widget_room].set_character(hermes_and_widget)
    
    if hermes.affinity == 1 and "art supplies" in backpack and current_room.get_character() == hermes_and_widget:
        print("As you enter the room, you feel your backpack begin to shake. Suddenly, the art supplies you were carrying burst out on their own!")
        time.sleep(3)
        print("The paints begin to pour themselves into puddles on the floor and the brushes whiz about the room, using the paints to create intricate runes and sigils, similar to the ones you saw in the attic.")
        time.sleep(3)
        print("As the chaos erupts around you, you begin to notice a ghostly figure taking shape, controlling the brushes.")
        time.sleep(3)
        print("The room is now almost completly covered with the paintings when the ethereal artist (who you can only assume to be the \"Smudge\" which signed all the paintings in the attic) stops suddenly.")
        time.sleep(3)
        print("In the sudden stillness, Widget lets out a meow (or was it a, \"Hello\"?), causing you to nearly jump out of your skin.")
        time.sleep(3)
        print("Suddenly, the artist looks at the cat and says, \"Oh, right!\" and gives a final flourish of paint.")
        time.sleep(3)
        print("The artist formerly known as Smudge steps back and Widget darts past Hermes into the center of the room.")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("You look on in shock and horror as Widget starts to morph and change shape, growing steadily larger.")
        time.sleep(3)
        print("You shield your eyes from a blinding flash of light, and when you look back, Widget is gone. In his place stands a handsome gentleman in a tuxedo.")
        time.sleep(3)
        print("He holds out his hand and says, \"It's " + player_name + ", right? I'm Henry Baker, thank you so much for your help! I transfigured myself into a cat and couldn't manage to turn myself back. It's great to be a human again!\"")
        time.sleep(3)
        print("As he recounts his tale, you hear a faint, repetitive buzzing sound. It steadily grows louder and louder, until it's almost deafening.")
        time.sleep(3)
        print("Curiously though, no one else seems to hear it...")
        time.sleep(3)
        print("You open your mouth to ask Mr. Baker if he can hear it, when suddenly...")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(3)
        print("...")
        time.sleep(4)
        print("...")
        time.sleep(5)
        print("You wake up.")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("")
        time.sleep(1)
        print("What a weird dream...")
        time.sleep(1)
        print("")
        print("")
        print("")
        print("~~YOU WIN!~~")
        time.sleep(10)
        break


    
print("")
print("")
print("")    
RPGInfo.credits()