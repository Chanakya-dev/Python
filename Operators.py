# Arithmetic Operators
a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a // b)  # Floor Division: 3
print(a % b)   # Modulus: 1
print(a ** b)  # Exponentiation: 1000

# Comparison Operators
x = 5
y = 10

print(x == y)  # Equal to: False
print(x != y)  # Not equal to: True
print(x > y)   # Greater than: False
print(x < y)   # Less than: True
print(x >= y)  # Greater than or equal to: False
print(x <= y)  # Less than or equal to: True

# Logical Operators
x = True
y = False

print(x and y)  # Logical AND: False
print(x or y)   # Logical OR: True
print(not x)    # Logical NOT: False

# Bitwise Operators

a = 5  # (binary: 0101)
b = 3  # (binary: 0011)

print(a & b)  # AND: 1 (binary: 0001)
print(a | b)  # OR: 7 (binary: 0111)
print(a ^ b)  # XOR: 6 (binary: 0110)
print(~a)     # NOT: -6 (inverts all bits)
print(a << 1) # Left Shift: 10 (binary: 1010)
print(a >> 1) # Right Shift: 2 (binary: 0010)

# Assignment Operators
a = 10

a += 5   # a = a + 5 -> 15
print(a)

a -= 3   # a = a - 3 -> 12
print(a)

a *= 2   # a = a * 2 -> 24
print(a)

a /= 4   # a = a / 4 -> 6.0
print(a)

a %= 4   # a = a % 4 -> 2.0
print(a)

a **= 3  # a = a ** 3 -> 8.0
print(a)



# Identify Operators

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is z)   # True (same object)
print(x is y)   # False (different objects, same content)
print(x is not y)  # True

# Membership Operators
fruits = ['apple', 'banana', 'cherry']

print('apple' in fruits)  # True
print('orange' in fruits) # False
print('orange' not in fruits) # True

