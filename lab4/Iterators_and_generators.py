#exercise 1:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#exercise 2:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#exercise 3:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#exercise 4:
mystr = "banana"

for x in mystr:
  print(x)

#exercise 5:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    x = self.a
    self.a += 1
    return x
  
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#exercise 6:
class MyNumber:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x 
    else:
      raise StopIteration
    
myclass = MyNumber()
myiter = iter(myclass)

for x in myiter:
  print(x)