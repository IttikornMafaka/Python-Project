import random

print('''                     
\ \      / /__| | ___ ___  _ __ ___   ___  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/ 
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| 
'''
)
print("Welcome to Rock, Paper, Scissors Game !!!")
print(input("Enter your name : ")," Let's start the game...")
user_choice = (input("Which do you choose? Rock, Paper or Scissors? : ")) #Input from user

Rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')            # ascii art for Rock

Paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')        # ascii art for Paper

Scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')        # ascii art for Scissors

# Convert user input to corresponding number
if user_choice == "Rock":
    user_choice = 0
elif user_choice == "Paper":
    user_choice = 1
elif user_choice == "Scissors":
    user_choice = 2

# Display user's choice
image_game = [Rock, Paper, Scissors]
if user_choice >= 0 and user_choice <= 2:
    print(image_game[user_choice])

# Generate computer's choice
computer_choice = random.randint(0,2)
print("Computer chose:",image_game[computer_choice])

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 0 and computer_choice == 2 :
    print("You Win !")
elif user_choice == 2 and computer_choice == 0 :
    print("You loose!")
elif user_choice > computer_choice :
    print("You win!")
elif user_choice < computer_choice:
    print("You lose!")
else :
    print("Wrong Command !!!")