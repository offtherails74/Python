# Part 1 - For Loops

# Create the list of heights
heights = [1.82, 1.75, 1.68, 1.76, 1.5]

# 1. Print all values from the heights list
print("All heights:")
for height in heights:
    print(height)

# 2. Print only values that are greater than 1.75
print("\nHeights greater than 1.75:")
for height in heights:
    if height > 1.75:
        print(height)

# 3. Print all values until reaching the 1.68 value (inclusive)
print("\nHeights until reaching 1.68 (inclusive):")
for height in heights:
    print(height)
    if height == 1.68:
        break

# 4. Print all values without the value of 1.68
print("\nHeights excluding 1.68:")
for height in heights:
    if height != 1.68:
        print(height)


# Part 2 - While Loops

# 1. Create a while loop that prints a variable named i until it reaches the number 4
i = 0
print("Printing i until it reaches 4:")
while i < 4:
    print(i)
    i += 1

# 2. Use a while loop to print out only even numbers lower than 15
print("\nEven numbers lower than 15:")
j = 0
while j < 15:
    if j % 2 == 0:  # Check if j is even
        print(j)
    j += 1

# 3. Use a while loop to print all numbers lower than 15, but skipping numbers 1-5
print("\nNumbers lower than 15, skipping 1-5:")
k = 0
while k < 15:
    if k > 5:  # Skip numbers 1-5
        print(k)
    k += 1


# Part 3 - Actors

# Lists of actors and their corresponding roles
actors = [
    "Nathan Fillion",
    "Gina Torres",
    "Alan Tudyk",
    "Morena Baccarin",
    "Adam Baldwin",
    "Jewel Staite",
    "Sean Maher",
    "Summer Glau",
    "Ron Glass"
]

roles = [
    "Captain Malcolm Reynolds",
    "Zoe Washburn",
    "Hoban Washburn",
    "Inara Serra",
    "Jayne Cobb",
    "Kaylee Frye",
    "Dr. Simon Tam",
    "River Tam",
    "Derrial Book"
]

# Print out each actor with their corresponding role
for i in range(len(actors)):
    print(f"{actors[i]} as {roles[i]}")
#____________________________________________________________________________________