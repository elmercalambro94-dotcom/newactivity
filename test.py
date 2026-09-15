class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.1416 * self.r ** 2

    def __str__(self):
        return f"Circle(area={self.area():.1f})"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def __str__(self):
        return f"Square(area={self.area():.1f})"


def print_area(shape):
    print(shape, "-> area:", shape.area())


for s in [Circle(3), Square(4)]:
    print_area(s)