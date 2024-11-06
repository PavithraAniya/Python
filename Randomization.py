# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random
#random.random() --> will print random float numbers between 0 & 1 excluding ranges numbers
rand_num = random.randint(0,1) # integer function include range numbers as well
#print(rand_num)
if rand_num==1:
  print("Heads")
else:
  print("Tails")

