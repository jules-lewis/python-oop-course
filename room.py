class Room():
    def __init__(self, room_name = None, room_description = None):
        self.name = room_name
        self.description = room_description
        self._linked_rooms = {}
        
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, room_description):
        self._description = room_description

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, room_name):
        self._name = room_name

    def describe(self):
        print(40 * "-")

        if self._name == None:
            print("No name set.")
        else:
            print(self._name)
        
        if self._description == None:
            print("No description set.")
        else:
            print(self._description)
        
        for direction in self._linked_rooms:
            room = self._linked_rooms[direction]
            print( "The " + room.name + " is " + direction)
        print(40 * "-")
        print()

    def link_room(self, room_to_link, direction):
        self._linked_rooms[direction] = room_to_link

    def move(self, direction):
        if direction in self._linked_rooms:
            return self._linked_rooms[direction]
        else:
            print()
            print("You can't go that way")
            return self



