from room import Room

kitchen = Room("Kitchen")
kitchen.description = "A dank and dirty room buzzing with flies"

dining_hall = Room("Dining Hall")
dining_hall.description = "A large room with ornate golden decorations on each wall."

ballroom = Room("Ballroom")
ballroom.description = "A vast room with a shiny wooden floor. Huge candlesticks guard the entrance."

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")

ballroom.link_room(dining_hall, "east")
dining_hall.link_room(ballroom, "west")

kitchen.describe()
dining_hall.describe()
ballroom.describe()










