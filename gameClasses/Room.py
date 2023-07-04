from gameClasses.Thing import Thing


class Room(Thing):
    def __int__(self, name, description, n, s, e, w, ne, nw, se, sw, up, down):
        super().__init__(name, description)
        self._n = n
        self._s = s
        self._e = e
        self._w = w

        self._ne = ne
        self._nw = nw
        self._se = se
        self._sw = sw

        self._up = up
        self._down = down

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        self._n = value

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        self._s = value

    @property
    def e(self):
        return self._e

    @e.setter
    def e(self, value):
        self._e = value

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        self._w = value
