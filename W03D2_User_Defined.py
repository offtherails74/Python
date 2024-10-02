

def greet(name):
    print(f"Hello, {name}! Welcome to our community.")
    print(f"Hope you have a wonderful day, {name}.")
    print(f"It's great to see you, {name}!")

# List
names = ["Alice", "Bob", "Charlie"]

# Loop through list
for person in names:
    greet(person)


# 1. Function to print full name
def print_full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    print(f"Hello, {full_name}.")

# 2. Function to add two numbers and print the result
def add_and_print(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")

# 3. Modified addition function to return the sum
def add_numbers(num1, num2):
    return num1 + num2

# 4. Function to sum all numbers in a list
def sum_list(numbers):
    return sum(numbers)

# 5. Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Example usage of each function:

# 1. Print full name
print_full_name("John", "Doe")

# 2. Add two numbers and print
add_and_print(4, 5)

# 3. Return the sum of two numbers
result = add_numbers(10, 20)
print(f"The returned sum is: {result}")

# 4. Sum all numbers in a list
numbers_to_sum = [1, 2, 3, 4, 5]
total = sum_list(numbers_to_sum)
print(f"The sum of the list is: {total}")

# 5. Reverse a string
sample_string = "Hello, World!"
reversed_str = reverse_string(sample_string)
print(f"The reversed string is: '{reversed_str}'")
