# If Block
x= 10

if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

# If Else
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")  # Output: x is 5 or less

# If elif else
x = 20

if x < 10:
    print("x is less than 10")
elif x == 20:
    print("x is 20")  # Output: x is 20
else:
    print("x is greater than 20")

# Nested If
x = 15

if x > 10:
    if x < 20:
        print("x is between 10 and 20")  # Output: x is between 10 and 20

# Loops

# For Loop
# Example 1: Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple, banana, cherry

# Example 2: Use range
for i in range(5):  # Range: 0 to 4
    print(i)  # Output: 0 1 2 3 4


# While Loop
x = 5
while x > 0:
    print(x)  # Output: 5 4 3 2 1
    x -= 1

# break
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0 1 2

# continue
for i in range(5):
    if i == 3:
        continue
    print(i)  # Output: 0 1 2 4

# Combining Loops and Conditions
for num in range(1, 11):  # Loop through numbers 1 to 10
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Nested Loops

# Simulate a 24-hour clock with hours, minutes, and seconds
for hour in range(0, 24):  # Outer loop for hours (0 to 23)
    for minute in range(0, 60):  # Middle loop for minutes (0 to 59)
        for second in range(0, 60):  # Inner loop for seconds (0 to 59)
            print(hour, "hours", minute, "minutes", second, "seconds")
