# Variables
name = "John"
age = 25
height = 1.75
is_student = True

# Printing
print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")

# Control Flow with elif
age = 25

if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Lists and Loops
fruits = ["apple", "banana", "orange"]

# Loop through list
for fruit in fruits:
    print(fruit)

# While loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

# Call function
result = greet("Alice")
print(result)

# Libraries
import random

# Generate a random number
random_number = random.randint(1, 10)
print(f"Random Number: {random_number}")

# For loop to print even numbers from 0 to 10
for number in range(11):
    if number % 2 == 0:
        print(number)