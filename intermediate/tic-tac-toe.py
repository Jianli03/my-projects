board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def display_board(board):
  for row in board:
    for cell in row:
      print(cell, end=" ")
    print()

def get_player_move(player):
  while True:
    row = int(input(f"Player {player}, enter row number (1-3): ")) - 1
    col = int(input(f"Player {player}, enter column number (1-3): ")) - 1
    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == '-':
      return row, col
    else:
      print("Invalid move. Try again.")


def place_mark(board, player, row, col):
  board[row][col] = player


def check_winner(board, player):
  # Check rows and columns
  for i in range(3):
    if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
      return True

  # Check diagonals
  if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
    return True

  return False

def main():
  current_player = 'X'
  while True:
    display_board(board)
    row, col = get_player_move(current_player)
    place_mark(board, current_player, row, col)

    if check_winner(board, current_player):
      display_board(board)
      print(f"Player {current_player} wins!")
      break

    # Check for tie (all cells filled)
    if all(cell != '-' for row in board for cell in row):
      display_board(board)
      print("It's a tie!")
      break

    current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
  main()