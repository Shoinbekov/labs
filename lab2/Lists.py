#exercise 1:
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#exercise 2:
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)

#exercise 3:
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#exercise 4:
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)

#чтобы добавить элементы из другого списка в текущий список
"""
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
"""

#exercise 5:
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

#exercise 6:
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#exercise 7:
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#exercise 8:
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
