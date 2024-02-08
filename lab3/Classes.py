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
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.length * self.width

    def a(self):
        print("Area of the rectangle is {}".format(self.area))

rectangle = Rectangle(5, 10)
rectangle.a()

#exercise 4:
import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Point coordinates: ({}, {})".format(self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)
p1 = Point(3, 4)
p2 = Point(6, 8)
p1.show()
p1.move(1, 1)
p1.show()
print("Distance between p1 and p2 is {}".format(p1.dist(p2)))

#exercise 5:
class Account():
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} has been deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} has been withdrawn. New balance: {self.balance}")
            else:
                print("Withdrawal amount exceeds available balance.")
        else:
            print("Withdrawal amount must be greater than 0.")

    def show_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Account balance: {self.balance}")
name_secondname = Account("Name Seconname", 500)
name_secondname.deposit(500)
name_secondname.withdraw(200)
name_secondname.show_balance()

#exercise 6:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime_numbers = list(filter(lambda n: is_prime(n), numbers))
print(prime_numbers)