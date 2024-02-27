class Shape:
    def get_area(self):
        pass

class Circle(Shape):
    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Triangle(Shape):
    def set_base_and_height(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

class Polygon(Shape):
    def set_side_lengths(self, sides):
        self.sides = sides

    def get_area(self):
        return 10

def main():
    circle = Circle()
    rectangle = Rectangle()
    triangle = Triangle()
    polygon = Polygon()

    circle.set_radius(5)
    rectangle.set_width(4)
    rectangle.set_height(6)
    triangle.set_base_and_height(4, 3)
    polygon.set_side_lengths([3, 4, 5])

    print("Circle Area:", circle.get_area())
    print("Rectangle Area:", rectangle.get_area())
    print("Triangle Area:", triangle.get_area())
    print("Polygon Area:", polygon.get_area())

if __name__ == "__main__":
    main()
