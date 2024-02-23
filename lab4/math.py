#exercise 1:
import math
degree = float(input("Input degree: "))
radian = degree*(math.pi/180)
print("Output radian: ",radian)

#exercise 2:
import math
height = int(input("Height: "))
base = int(input("Base, first value: "))
base2 = int (input("Base, second value: "))
area = (((base+base2)/2)*height)
print("Expected Output: ", area)

#exercise 3:
import math

sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
apothem = length / (2 * math.tan(math.pi / sides))
area = int((sides * length * apothem) / 2)

print("The area of the polygon is:", area)

#exercise 4:
import math
base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))
area = float(base*height)
print("Expected Output: ",area)