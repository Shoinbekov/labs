#exercise 1:
def myfunc():
  x = 300
  print(x)

myfunc()

#exercise 2:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#exercise 3:
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#exercise 4:
x = 300

def myfunc():
  x = 200
  print(x)

myfunc(
)