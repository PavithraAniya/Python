# names_string = "Angela", "Ben", "Jenny"
# names= names_string.split(", ")

import random

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
person_who_will_pay= names[random_choice]

print(person_who_will_pay+ " is going to buy the meal today!")
