import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 5

# reels
rows = 3
cols = 3

# symbols tables on reels
symbols  = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8,
}


# get random symbols list after a spin
def get_slot_spin(row, cols, symbols):
    all_symbols = []

    for symbol, value in symbols.items():
        for _ in range(value):
            all_symbols.append(symbol)


    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]  # make a copy of all_symbols
        for row in range(rows):
            value = random.choice(current_symbols)
            all_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def display_reels(symbols):
  """Displays the slot machine reels with visual formatting.

  Args:
      symbols (list): A list representing the current symbols on the reels.
  """
  for row in symbols:
    print("|" + "|".join(row) + "|")  # Align symbols with pipes


def check_win(symbols):
  if symbols[0] == symbols[1] == symbols[2]:  # All symbols match
    return "Win!"
  else:
    return "Sorry, no win this time."


def play_again():
  """Prompts the user to play another round."""
  choice = input("Play again? (y/n): ").lower()
  return choice == "y"



def deposite():
    while True:
        amount = input("What would you like to desosit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Invalid amount. Try again.")
        else:
            print("Please enter a number.")
    return amount


def withdraw():
    return 0

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?  ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Invalid number of lines. Try again.")


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between $ {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number.")
    return amount

def main():
    """Main function to run the slot machine simulation."""
    print("Welcome to the Slot Machine!")

    while True:
        balance = deposite()
        lines = get_number_of_lines()

        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough to bet, Your balance is ${balance}.")
        else:
            break

    print(f"Your balance is ${balance}. You are betting with ${bet}, on {lines} lines."  )

    while True:
        random_symbols = get_slot_spin(rows, cols, symbols)
        display_reels(random_symbols)
        result = check_win(random_symbols)
        print(result)
        if not play_again():
            break
    print("Thanks for playing!")




main()