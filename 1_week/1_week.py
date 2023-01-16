## 1 week ##

# input and print result
a, b = map(int, input().split())
print(a+b)

# input and print result
a, b = map(int, input().split())
print(a-b)

# Given two integers A and B, write a program that compares A and B.
a, b = map(int, input().split())

if a > b:
    print('>')
elif a == b:
    print('==')
else:
    print('<')

# Write a program that receives test scores and outputs an A for 90-100 points, a B for 80-89 points, a C for 70-79 points, a D for 60-69 points, and an F for the remaining scores.
score = int(input())

if 90 <= score <= 100:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('F')

# One common math problem is figuring out which quadrant a given point falls into. The quadrants are numbered 1 through 4 as shown in the figure below. "Quadrant n" means "the nth quadrant".
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')

# Write a program that, when given a year, prints 1 if it is a leap year or 0 otherwise.

year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(1)
else:
    print(0)

# Given a natural number N, write a program that prints the numbers 1 through N, one per line.

n = int(input())
for i in range(1, n+1):
    print(i)

# Given an integer N greater than or equal to 0. At this time, write a program that outputs N!

n = int(input())
result = 1
if n > 0:
    for i in range(1, n+1):
        result = result * i
print(result)

# Write a program that takes two integers A and B as input and outputs A+B.

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a + b)

# Write a program that takes two integers A and B as input and outputs A+B.
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)

# Write a program that receives N as input and outputs the N multiplication table. You have to print according to the output format.
n = int(input())
for i in range(1, 10):
    print(n, '*', i, '=', n * i)

# 1 star on the first line, 2 stars on the second line, and N stars on the Nth line.
n = int(input())
for i in range(1, n + 1):
    print('*' * i)

# Write a program that takes two integers A and B as input and outputs A+B.
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

# Given a sequence A of N integers and an integer X. At this time, write a program that prints all numbers from A to X that are less than X.
n, x = map(int, input().split())
array = map(int, input().split())
for i in array:
    if i < x:
        print(i, end=' ')

# Write a program to find how many integers v are given a total of N integers.
n = int(input())
array = [int(i) for i in input().split()][:n]
v = int(input())
print(array.count(v))

# Write a program to find the attendance numbers of 2 students who did not submit the special assignment assigned by the professor among 28 students.
students = list(range(1, 31))
for i in range(28):
    student = int(input())
    del students[students.find(student)]
for student in students:
    print(student)

# Given two matrices A and B of size N*M, write a program that adds two matrices.
x, y = map(int, input().split())
array = [[] for i in range(2)]
for count in range(2):
    for i in range(x):
        array[count].append([int(i) for i in input().split()])
for c in range(x):
    for r in range(y):
        print(array[0][c][r] + array[1][c][r], end=' ')
    print()

# Write a program that outputs the ASCII code value of the given letter when one of the lowercase letters, uppercase letters, and numbers 0-9 is given.
s = ord(input())
print(s)