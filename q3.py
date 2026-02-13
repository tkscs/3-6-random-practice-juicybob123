import random
suits = "♠♥♣♦"

values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = []
# Make a deck of cards
# `deck` should be a list of strings with a value and a suit, e.g. "4♣"

#shuffle your `deck` and print it out
for i in range(5):
    string = [f"{random.choice(values)}, {random.choice(suits)}"]
    deck + string
    if string in deck:
        print(f"{random.choice(values)}, {random.choice(suits)}")
    else:
        print(string)
    
# sample a hand of 5 cards and print it out
# (WITHOUT replacement -- no repeats!)