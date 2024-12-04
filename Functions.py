# 1. Function Without Parameters
def say_hello():
    print("Hello, World!")

# Call the function
say_hello()  # Output: Hello, World!


# 2. Function With Parameters
def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet("Alice")  # Output: Hello, Alice!


# 3. Function with Return Statement
def add_numbers(a, b):
    return a + b

# Call the function and use its return value
result = add_numbers(5, 3)
print(result)  # Output: 8


# 4. Multi-Keyword Arguments (Keyword Arguments Using **kwargs)
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function
print_details(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York


# 5. Multi Non-Keyword Arguments (Positional Arguments Using *args)
def sum_numbers(*args):
    return sum(args)

# Call the function
result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15


# 6. Combining Positional (*args) and Keyword (**kwargs) Arguments
def describe_person(*args, **kwargs):
    print("Positional arguments (hobbies):", args)
    print("Keyword arguments (details):", kwargs)

# Call the function
describe_person("reading", "coding", name="Alice", age=25)
# Output:
# Positional arguments (hobbies): ('reading', 'coding')
# Keyword arguments (details): {'name': 'Alice', 'age': 25}

