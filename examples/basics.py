# This script demonstrates basic Python programming constructs.
# Run this using `python examples/basics.py`

# Variables
x = 10  # integer
y = 3.14  # float
name = "Alice"  # string
is_student = True  # boolean

# Print statements
print("Hello, World!")
print("x:", x)
print("y:", y)
print("name:", name)
print("is_student:", is_student)

# Basic arithmetic operations
sum_result = x + y
difference = x - y
product = x * y
quotient = x / y
remainder = x % y

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Remainder:", remainder)

# Lists
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])

# Adding to a list
fruits.append("date")
print("Fruits after adding date:", fruits)

# Removing from a list
fruits.remove("banana")
print("Fruits after removing banana:", fruits)

# Dictionaries
student = {
    "name": "Bob",
    "age": 20,
    "courses": ["Math", "Science"]
}
print("Student:", student)
print("Student's name:", student["name"])

# Adding to a dictionary
student["grade"] = "A"
print("Student after adding grade:", student)

# Removing from a dictionary
del student["age"]
print("Student after removing age:", student)

# If-else statements
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# For loop
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Classes and objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.bark())
