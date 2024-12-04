# 1. Assigning Values to Variables

# Assigning values to variables
p = 90        # p is assigned the value 90
p = "Siva"    # p is reassigned a new value "Siva"
b = "Mani"    # b is assigned the value "Mani"
c = p + b     # c concatenates p ("Siva") and b ("Mani")

# Concatenating strings
p = p + " Mani"
print(p)  # Output: Siva Mani


# 2. Assigning the Same Value to Multiple Variables

# Assigning the same value to multiple variables
a = b = c = 10
print(b)  # Output: 10
print(a)  # Output: 10
print(c)  # Output: 10

# Assigning different values to multiple variables in a single line
a, b, c = 5, 4, 3
print(a, b, c)  # Output: 5 4 3

# Summing the values of a, b, and c
print(a + b + c)  # Output: 12


# 3. Type Casting

# Casting an integer to float
a = 32
b = float(a)  # Converts integer to float
print(a)  # Output: 32 (Original value of a)
print(a, b)  # Output: 32 32.0

# Casting to string
a = float(a)  # Converting a to float again
print(a, b)  # Output: 32.0 32.0

# Converting to string
c = str(a)  # Converting float to string
print(c)  # Output: "32.0"
print(type(c))  # Output: <class 'str'>

# String concatenation
c = c + " Charan"
print(c)  # Output: "32.0 Charan"


# 4. Boolean Conversion

# Converting a non-zero number to a boolean (True)
f = 2
f = bool(f)  # Converts f to boolean (True)
print(f)  # Output: True

# Converting an empty string to a boolean (False)
op = ""
p = bool(op)  # Converts empty string to boolean (False)
print(p)  # Output: False


# 5. User Input and Casting

# Taking user input and converting it to different types

# Input for name (String)
name = input("Enter Your Name: ")
print(name)

# Input for id (Integer)
y = int(input("Enter your ID: "))
print(y)

# Input for score (Float)
z = float(input("Enter your score: "))
print(z)
