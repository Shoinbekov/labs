#exercise 1:
N=int(input())
def generate_squares(N):
    for i in range(1, N + 1):
        yield i**2
squares_generator = generate_squares(N)
for square in squares_generator:
    print(square)

#exercise 2:
def range(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


numbers = range(10)
print(*numbers, sep=", ")

#exercise 3:
def divisible_by3_and4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


print(*divisible_by3_and4(30), sep=", ")

#exercise 4:
def squares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2


print(*squares(10, 20))

#exercise 5:
def reduce(n):
    for i in range(0, n):
        yield n - i
print(*reduce(10), sep=", ")