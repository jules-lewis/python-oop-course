class Item():
    def __init__(self, item_name, item_description = None):
        self.name = item_name
        self._description = item_description
        
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, item_description):
        self._description = item_description

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, item_name):
        self._name = item_name

    def describe(self):
        print(40 * "-")
        print(self._name)
        if self._description is not None:
            print(self._description)
        print(40 * "-")
        print()
