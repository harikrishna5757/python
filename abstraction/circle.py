from shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print(3.14 * self.radius * self.radius)


c = Circle(3)
c.calculate_area()
