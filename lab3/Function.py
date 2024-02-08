#exercise 1:
def grams_to_ounces(grams):
    ounces=28.3495231 * grams
    return ounces
grams = float(input())
ounces=grams_to_ounces(grams)
print(f"{grams} grams = {ounces} ounces")

#exercise 2: 
def temperature(F):
    C = (5 / 9) * (F - 32)
    return C
F = float(input())
centigrade = temperature(F)
print(f"temperature in centigrade is  {centigrade} ")

#exercise 3:
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if(2 * chickens + 4 * rabbits)==numlegs:
            return chickens, rabbits
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(f"chickens = {result[0]}, rabbits = {result[1]}")  

#exercise 4:
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print((filter_prime(nums)))

#exercise 5:
from itertools import permutations
def string_perm(s):
    perm = permutations(s)
    for p in perm:
        print(''.join(p))
x = str(input())
string_perm(x)

#exercise 6:
def reverse_words(s):
    words = s.split()
    reversed_words = " ".join(reversed(words))
    return reversed_words

sentence = str(input()) #or as given in example we can use "We are ready"
reversed_sentence = reverse_words(sentence)
print(reversed_sentence) 
    
#exercise 7:
def has_33(n):
    for i in range(len(n)-1):
        if n[i] == 3 and n[i+1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#exercise 8:
def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#exercise 9:
import math
def sphere(r):
    volume = (4/3) * math.pi * (r ** 3)
    return volume
n = float(input())
print(sphere(n))

#exercise 10:
def unique_list(l):
    u_list = []
    for i in l:
        if i not in u_list:
            u_list.append(i)
    return u_list
l = [1, 2, 3, 4, 2, 3, 5, 6, 5]
print(unique_list(l))

#exercise 11:
def palindrome(p):
    p = p.lower().replace(" ", "")
    return p == p[::-1]
p = str(input())
print(palindrome(p))

#exercise 12:
def histogram(s):
    for i in s:
        print("*" * i)
s = [4, 9, 7]
print(histogram(s))

#exercise 13:
import random 
def random_number_guess():
    name = input("Hello! What is your name ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    num = random.randint(1, 20)
    num_to_guess = 0
    while True:
        guess = int(input("Take guess: "))
        num_to_guess+=1
        if guess < num:
            print("Your guess is too low.")
        elif guess > num:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_to_guess} guesses!")
            break
random_number_guess()