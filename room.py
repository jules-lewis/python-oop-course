class Room():
    def __init__(self, room_name = None):
        self.name = room_name
        
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, room_description):
        self._description = room_description

