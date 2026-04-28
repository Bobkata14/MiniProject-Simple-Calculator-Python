#NUMBERS
#Three numeric types in Python
"""
x = 1 #int
y = 1.20 #float
z = 1j #complex

print(type(x))
print(type(y))
print(type(z))
"""

#int or integer is a whole number positive or negative without decimals of unlimited length.
"""
x = 1
y = 313511513135
z = -321351353

print(type(x))
print(type(y))
print(type(z))
"""

#Float or "floating point number" is a number, positive or negative, containing one more decimals.
"""
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
"""

#Float can also be scientific numbers with an "e" to indicate the power of 10.
"""
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
"""

#Complex numbers are written with a "j" as the imaginary part:
"""
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
"""

#Type convertion
"""
x = 1
y = 1.2
z = 1j

#Convert form int to float:
a = float(x)

#Convert from float to int:
b = int(y)

#Convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
#Cannot convert complex numbers into another number type!
"""

"""Python does not have a random() function to make a random number,
but Python has a built-in module called random that can be used to make random numbers:"""

""""
import random
print(random.randrange(1, 10))
"""

#CASTING
"""int() - construct an integer number from an integer literal , a float literal (by removing all decimals),
or a string literal (providing the string represents a whole number)."""
"""
x = int(1)
y = int(2.8)
z = int("3")

print(x)
print(y)
print(z)
"""

"""float() - constructs a float number from an integer literal, a float literal or a string literal
(providing the string represents a float ot an integer)."""
"""
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")

print(x)
print(y)
print(z)
print(w)
"""

#str() - constrict a string from a wide variety of data types, including strings, integer literals and float literals.
"""
x = str("s1")
y = str(2)
z = str(3.0)

print(x)
print(y)
print(z)
"""

#Exercise 1
x = 10   #int
y = 5.5  #float
z = 2j   #complex

#Exercise 2
x = 10
y = 5.5
z = 2j

print(type(x))
print(type(y))
print(type(z))


#Exercise 3
x = 5

a = float(x)

print(a)

#Exercise 4
y = 7.9

b = int(y)

print(b)

#Exercise 5
num = 100

c = str(num)

print(c)

#Exercise 6
x = 5
y = 2.5

print(x + y) #The result will be 7.5 float number

#Exercise 7
age = "20"
new_age = int(age) + 5
print(new_age)


#Exercise 8
a = 10
b = 3

print(f"Addition: {a+b}")
print(f"Subtraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Division: {a/b}")

#Overall - 6.00