#exercise 1:
from functools import reduce
from operator import mul
import time
import math
def multiply_list(numbers):
    return reduce(mul, numbers)


numbers = [1, 2, 3, 4, 5]
print(multiply_list(numbers))

#exercise 2:
from functools import reduce
from operator import mul
import time
import math
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower


s = "Salem, alem"
upper, lower = count_case(s)
print(f"Upper case letters: {upper}, Lower case letters: {lower}")

#exercise 3:
from functools import reduce
from operator import mul
import time
import math
def ispolindrome(a):
    return a == "".join(reversed(a))

print(ispolindrome("level"))
print(ispolindrome("moon"))

#exercise 4:
from functools import reduce
from operator import mul
import time
import math
def delayed_sqrt(n, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(n)


n = 25200
delay_ms = 2123
result = delayed_sqrt(n, delay_ms)
print(f"Square root of {n} after {delay_ms} milliseconds is {result}")

#exercise 5:
from functools import reduce
from operator import mul
import time
import math
def true(elements):
    return all(elements)

print(true((True, True, True)))
print(true((True, False, True)))