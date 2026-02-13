# Make a random pet.
import random
# Choose:
# Type of animal (at least 3 choices, string)
animal = random.choice(["dog", "cat", "mule"]) 
# Age (integer)
age = random.randint(0,20)
# Color (at least 3 choices, string)
colour = random.choice(["blue", "blace","red", "white," "brown"])
# Weight (float)
weight =random.randint(20,500)

# Print a summary of your pet using an f-string
print(f"Your pet is a {animal} and is {age} years old, and is {colour} colored its weight is {weight}lbs")#REPLACE THIS WITH YOUR CODE