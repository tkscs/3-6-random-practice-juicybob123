import random

def spin_twister_spinner():

  """
  Returns a list with a random color, side, and appendage
  
  colors: "red", "green", "yellow", or "blue"
  sides: "left" or "right"
  appendage: "hand" or "foot"
  """
  #YOUR CODE HERE
  colors = ["red", "green", "yellow", "blue"]
  sides = [ "left", "right"]
  appendage = ["hand", "foot"]
  print(random.choices(colors, k=1))
  print(random.choices(sides, k=1))
  print(random.choices(appendage,k= 1))

# Here's the function call. This should print a random assortment of twister commands
for _ in range(10):
  print(spin_twister_spinner())