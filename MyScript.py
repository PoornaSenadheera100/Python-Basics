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

# Bitwise left shift
x = 5
print(x << 3)

# x = 00000101 -> 00101000 = 40