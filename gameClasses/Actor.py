from gameClasses.Thing import Thing


class Actor(Thing):
    def _init__(self, name, description, location):
        super().__init__(name, description)
        self._location = location

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
