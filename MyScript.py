# Display "Hello World"
print("Hello World")

# ================================================================================= #

# Display "Hello World with an empty line"
print("Hello World\n")

# ================================================================================= #

# Keep an empty line
print("\n")

# ================================================================================= #

# Expression
x = 1 + 2 ** 3 / 4 * 5
print(x)

# ================================================================================= #

# Enter two inputs and print the summation 
num1 = input("Enter a number: ")
print(num1)

num2 = input("Enter a number: ")
print(num2)

tot = int(num1) + int(num2)
print("Total:",tot)

# ================================================================================= #

# Print the data type of a variable
print(type(5))
print(type(5.0))
print(type("5"))
print(type(5 + 8j))
print(type([4, 5, 6]))
print(type(5>6))

# ================================================================================= #

# Concatenate two strings
print("Poorna" + " Senadheera")

# ================================================================================= #

# is operator (to check whether the two object are referenced to a same object or not)
x = 5
y = 5
print(id(x))
print(id(y))
print(x is y)

y = 6
print(id(x))
print(id(y))
print(x is y)
print(x is not y)

# ================================================================================= #

# String is like an array
name = "High"
print(name)
print(name[0] + name[1])

# ================================================================================= #

# Assign the answer with decimal points
num = 5 / 3
print(num)

# ================================================================================= #

# Assign the answer without decimal points
num = 5 // 3
print(num)

# ================================================================================= #

# Assign the remainder value
num = 5 % 3
print(num)

# ================================================================================= #

# Get the power value
num = 5 ** 2
print(num)

# ================================================================================= #

# AND operator
value = 5 > 3 and 8 < 3
print(value)

# ================================================================================= #

# OR operator
value = 5 > 3 or 8 < 3
print(value)

# ================================================================================= #

# IN and NOT IN operators
list = ["mango", "apple"]
a = "apple"
c = "banana"
print(a in list)
print(c not in list)

# ================================================================================= #

# Binary AND operator
x = 5
y = 7
print(x & y)

# x -> 101
# y -> 111
#      101 -> 5

# ================================================================================= #

# Binary OR operator
x = 5
y = 7
print(x | y)

# x -> 101
# y -> 111
#      111 -> 7

# ================================================================================= #

# Binary XOR operator
x = 5
y = 7
print(x ^ y)

# x -> 101
# y -> 111
#      010 -> 2

# ================================================================================= #

# Bitwise right shift
x = 5
print(x >> 2)

# x = 00101 -> 00001 = 1

# ================================================================================= #

# Bitwise left shift (Binary)
x = 5
print(x << 3)

# x = 00000101 -> 00101000 = 40

# ================================================================================= #

# Basic if-elif-else statements
mark = 80

if mark >= 75:
    print("Grade is A")
elif mark >= 65:
    print("Grade is B")
elif mark >= 55:
    print("Grade is C")
elif mark >= 35:
    print("Grade is S")
else:
    print("Fail")

# ================================================================================= #

# Star pattern
val = int(input())
for y in range(0, val):
    for x in range (0, val):
        print('*',end='')
    print("")

# if val = 4
# ****
# ****
# ****
# ****

# ================================================================================= #

# Check whether a number is prime or not
i = int(input())
j = 2
while (j <= (i/j)):
    if not(i%j):
        print("Not a prime")
        break
    j = j + 1
if (j > i/j):
    print("Prime")

# ================================================================================= #

# Lists
my_list = [1, 2, 100.9, "Poorna"]
print(my_list)
print(my_list[2])
print(my_list[1:])
print(my_list[0:3])

my_list.append(30)
print(my_list)

my_list[2] = 101.7
print(my_list)

my_list.remove(2)
print(my_list)

del my_list[1]
print(my_list)

# ================================================================================= #

# 2D Lists
list2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list2D)
print(list2D[2][0],list2D[0][1])

list2D[1].append(6.1)
print(list2D)

print(len(my_list))

new_list = ['Hi']
old_list = ['Bye']
print(new_list*4)
print(new_list+old_list)

# ================================================================================= #

# List Operations
fruits = ['Mango', 'Banana', 'Apple']
print('Orange' in fruits)
print('Banana' in fruits)

for fruit in fruits:
    print(fruit)

print(fruits[-2])

#    0          1        2
# ['Mango', 'Banana', 'Apple']
#   -3         -2       -1

# ================================================================================= #

# Get even numbers
numlist = [2, 4, 6, 8, 3, 4, 2, 1]
evenlist = []

for num in numlist:
    if num % 2 == 0 and num not in evenlist:
        evenlist.append(num)

print(evenlist)

# ================================================================================= #

# Loops
for count in [1, 2, 3, 4, 5]:
    print(count)

for count in range(1,6):
    print(count)

for count in range(6):
    print(count)

for even in range(0, 11, 2):
    print(even)


num = 5
while num > 2:
    print(num)
    num-=1

# ================================================================================= #

# Nested Loops

for i in range(4):
    for j in range(4):
        print('*',end='')
    print('')

# ================================================================================= #

# break, continue and pass statements
for i in range(5):
    if i == 2:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

for i in range(5):
    if i == 2:
        pass        # To avoid the syntax errors (if we have not implemented this part yet)
    print(i)

# ================================================================================= #

# Inputs and Outputs

# Just take the input
input("Enter your name : ")

# ================================================================================= #

# Take the input and print
print(input("Enter your name : "))

name = input("Enter your name :")
print(name)

# ================================================================================= #

# Take an integer
num = int(input("Enter an integer number : "))
print(num)

# ================================================================================= #

# Outputs

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep=",")
print(1, 2, 3, 4, sep="#")
print(1, 2, 3, 4, end="*\n")
print(1, 2, 3, 4, end=' ')
print("Not in a new line")

a = 5
b = 6

print("a is {} and b is {}".format(a, b))
print("b is {1} and a is {0}".format(a,b))

# ================================================================================= #

# Functions

from math import pi


x = min(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
y = max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("The minimum number is", x, "and the maximum number is", y)
print("The minimum number is {} and the maximum number is {}.".format(x, y))

# ================================================================================= #

def msgPrint(msg):
    "Print a message"
    print(msg)
    return

msgPrint("Hello")

# ================================================================================= #

def printNames(*names):
    "Print any number of names"
    for name in names:
        print(name)
    return

printNames("Poorna", "Sanuthi", "Sathira", "Hilarina")

# ================================================================================= #

def calcAreaCircle(r):
    "Calculate and return the area of a circle"
    area = pi * r * r
    return area

print(calcAreaCircle(5))

# ================================================================================= #

# try-except block
print("X + 5 = 8")
try:
    num = int(input("Enter a suitable value for X : "))

    if num == 3:
        print("Answer is correct")
    else:
        print("Incorrect answer!")
except:
    print("Please enter an integer value...")

# ================================================================================= #

# File Handling
fileHandler1 = open("Myfile1.txt", "r")
content = fileHandler1.read()
print(content)
fileHandler1.close()

fileHandler2 = open("Myfile1.txt", "r")
firstLine = fileHandler2.readline()
print(firstLine)
secondLine = fileHandler2.readline()
print(secondLine)
fileHandler2.close()

fileHandler3 = open("MyCreatedFile", "w")
fileHandler3.write("This file was created by another process.\n")

name = "Poorna"
fileHandler3.write("My name is " + name + ".")