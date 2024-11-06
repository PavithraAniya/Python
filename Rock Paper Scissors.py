rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

list = [rock, paper, scissors]
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
print(f"User choice\n {list[user_choice]}")
computer_choice = random.randint(0, len(list) - 1)
print(f"computer choice\n {list[computer_choice]}")
if user_choice == computer_choice:
    print(f'Tie!')
elif user_choice == 0 and computer_choice == 1:
    print(f'You lose!')
elif user_choice == 0 and computer_choice == 2:
    print(f'You win!')
elif user_choice == 1 and computer_choice == 0:
    print(f'You Win!')
elif user_choice == 1 and computer_choice == 2:
    print(f'You lose!')
elif user_choice == 2 and computer_choice == 1:
    print(f'You Win!')
else:
    print(f'You lose')

