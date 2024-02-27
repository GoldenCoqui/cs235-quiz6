from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def get_area(self):
        # Dummy calculation for circle area
        return 3.14 * 5 * 5

class Square(Shape):
    def get_area(self):
        return 4 * 4

class Rectangle(Shape):
    def get_area(self):
        return 3 * 6

def main():
    circle = Circle()
    square = Square()
    rectangle = Rectangle()

    print("Circle Area:", circle.get_area())
    print("Square Area:", square.get_area())
    print("Rectangle Area:", rectangle.get_area())

if __name__ == "__main__":
    main()
