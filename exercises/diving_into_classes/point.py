class Point:
    """ a 3D representation of any given point"""

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        self._z = z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Point(x=self.x + other.x,
                     y=self.y + other.y,
                     z=self.z + other.z)

    def __sub__(self, other):

        return Point(x=self.x - other.x,
                     y=self.y - other.y,
                     z=self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(x=self.x * other.x,
                         y=self.y * other.y,
                         z=self.z * other.z)
        elif isinstance(other, int):
            return Point(x=self.x * other, y=self.y * other, z=self.z * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, Point):
            return Point(x=self.x * other.x,
                         y=self.y * other.y,
                         z=self.z * other.z)
        elif isinstance(other, int):
            return Point(x=self.x * other, y=self.y * other, z=self.z * other)
        else:
            return NotImplemented

    def __iter__(self):
        return iter((self.x, self.y, self.z))


def test_shifting():
    p1, p2, p3 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)
    p3 = p2 + p1
    print(p3)
    p4 = p3 - p1
    print(p3)
    print(p4)
    x = 3 * p1
    print(x)

    return (p3.x, p3.y, p3.z) == (5, 7, 9)


if __name__ == "__main__":
    # p1 = Point(1, 2, 3)
    # print(p1)
    # # Point(x=1, y=2, z=3)
    # p2 = Point(1, 2, 3)
    # print(p2)
    #
    # print(p1 == p2)
    #
    # print(p1 == p2)
    # print(p2)
    # # Point(x=4, y=2, z=3)
    # print(p1 + p2)
    # p3 = p1 - p2
    # print(p3)
    print(test_shifting())
