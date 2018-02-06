class Room():
    def __init__(self, room_name = None):
        self.name = room_name
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
        print(self._name)
        print(self._description)
        for direction in self._linked_rooms:
            room = self._linked_rooms[direction]
            print( "The " + room.name + " is " + direction)
        print(40 * "-")

    def link_room(self, room_to_link, direction):
        self._linked_rooms[direction] = room_to_link



