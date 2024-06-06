import random

user_wins = 0
computer_wins = 0
ties = 0

options = ["rock", "paper", "scissors"]

win_conditions = {
  "rock": ["scissors"],
  "paper": ["rock"],
  "scissors": ["paper"]
}

def get_user_choice():
  while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
      return None
    if user_input in options:
      return user_input
    else:
      print("Invalid input. Please try again.")

def get_computer_choice():
  return random.choice(options)

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "Tie"
  elif user_choice in win_conditions[computer_choice]:
    return "Win"
  else:
    return "Loss"

while True:
  user_choice = get_user_choice()
  if user_choice is None:
    break

  computer_choice = get_computer_choice()
  result = determine_winner(user_choice, computer_choice)

  if result == "Win":
    print(f"You win! {user_choice.capitalize()} crushes {computer_choice.capitalize()}.")
    user_wins += 1
  elif result == "Loss":
    print(f"You lose! {computer_choice.capitalize()} covers {user_choice.capitalize()}.")
    computer_wins += 1
  else:
    print(f"It's a tie! You both chose {user_choice.capitalize()}.")
    ties += 1

print("**Game Summary**")
print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
print(f"There were {ties} ties.")