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


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle(area={self.area():.1f})"


def print_area(shape):
    print(shape, "-> area:", shape.area())


for s in [Circle(3), Square(4), Rectangle(length=5, width=2)]:
    print_area(s)