class Room():
    def __init__(self, room_name = None):
        self.name = room_name
        
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
        print(40 * "-")

