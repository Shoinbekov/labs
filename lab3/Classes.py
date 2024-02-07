#exercise 1:
class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

# Example usage:
manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()

#exercise 2:
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


# Example usage:
shape = Shape()
print("Area of Shape:", shape.area())  # Output: Area of Shape: 0

square = Square(5)
print("Area of Square:", square.area())  # Output: Area of Square: 25

#exercise 3:

