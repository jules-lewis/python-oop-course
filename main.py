from room import Room
from item import Item
from character import Enemy, Friend

#Our weapons -- you will need to get these from the friendly characters
cheese = Item("Cheese", "A lovely smelly Gorgonzola!")
magic_bean = Item("Magic bean", "Maybe Jack left this behind...")
garlic = Item("Garlic", "Great for sorting out vampires")

#The baddies, and their weaknesses
dave = Enemy("Dave", "A smelly zombie")
dave.conversation = "Brrlgrh... rgrhl... brains..."
dave.weakness = cheese.name

tilda = Enemy("Tilda", "A poisonous toad")
tilda.conversation = "Ribbit..... ribbit....."
tilda.weakness = magic_bean.name

madge = Enemy("Madge", "A fearsome witch, Mildred's evil twin!")
madge.conversation = "Hubble bubble, toil and trouble!"
madge.weakness = garlic.name

#Some friendlier folk... they might be able to help you
fred = Friend("Fred", "A helpful giant")
fred.set_item_carried(cheese)

mildred = Friend("Mildred", "A wise witch, Madge's helpful twin.")
mildred.set_item_carried(garlic)

bascule = Friend("Bascule", "A curious fellow, with a kindly twinkle in his eyes.")
bascule.set_item_carried(magic_bean)

#the map -- remember to mix up the goodies and baddies!
kitchen = Room("Kitchen")
kitchen.description = "A dank and dirty room buzzing with flies"
kitchen.enemy = tilda
kitchen.friend = mildred

dining_hall = Room("Dining Hall")
dining_hall.description = "A large room with ornate golden decorations on each wall."
dining_hall.enemy = dave
dining_hall.friend = bascule

ballroom = Room("Ballroom")
ballroom.description = "A vast room with a shiny wooden floor. Huge candlesticks guard the entrance."
ballroom.enemy = madge
ballroom.friend = fred

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")

ballroom.link_room(dining_hall, "east")
dining_hall.link_room(ballroom, "west")

current_room = kitchen
current_room.describe()  

backpack = []

def describe_backpack():
    if len(backpack) == 0:
        print("There is nothing in your backpack.")
    else:
        print("You're now carrying " + ", ".join(i.name for i in backpack))

game_loop = True

while game_loop:		
    command = input("> ")
    if command == "help":
        print("Available commands are: north, east, south, west, talk, fight, hug, ask, backpack, help, hint, quit.")
    elif command in ["north", "east", "south", "west"]:
        current_room = current_room.move(command)
        current_room.describe()
    elif command == "talk":
        current_room.enemy.talk()
    elif command == "fight":
        if len(backpack) == 0:
            print("You have nothing to fight with!")
        else:
            print("What will you fight with?")
            fight_with = input()
            found_item = False
            for item in backpack:
                if item.name == fight_with:
                    found_item = True
                    current_room.enemy.fight(fight_with)
                    if current_room.enemy.enemy_count == 0:
                        print("Well done! You have defeated all the enemies!")
                        game_loop = False
            if not found_item:
                print("You don't have " + fight_with + " in your backpack.")
    elif command == "hug":
        current_room.friend.hug()
    elif command == "ask":
        friend_item = current_room.friend.ask()
        if friend_item is not None:
            backpack.append(friend_item)
            describe_backpack()
    elif command == "backpack":
        describe_backpack()
    elif command == "hint":
        if len(backpack) == 0:
            print("You don't get if you don't ask...")
        else:
            print("Could you use what's in your backpack in a fight?")
    elif command == "quit":
        game_loop = False
    else:
        print("I didn't recognise that command. Hint: try 'help'.")
    print()
