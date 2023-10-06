import random

board = [' ' for x in range(9)]

def print_board():
  row1 = '|' + board[0] + '|' + board[1] + '|' + board[2] + '|'
  row2 = '|' + board[3] + '|' + board[4] + '|' + board[5] + '|' 
  row3 = '|' + board[6] + '|' + board[7] + '|' + board[8] + '|'
  print()
  print(row1)
  print(row2) 
  print(row3)
  print()

def player_move(icon):
  print(f"Your turn player {icon}")  
  choice = int(input("Enter your move: "))
  if board[choice - 1] == ' ':
    board[choice - 1] = icon
  else:  
    print("Space already taken")
    player_move(icon)

def check_win():
  # check rows
  if board[0] == board[1] == board[2] != ' ':
    return board[0]
  elif board[3] == board[4] == board[5] != ' ':
    return board[3]  
  elif board[6] == board[7] == board[8] != ' ':
    return board[6]

  # check columns  
  elif board[0] == board[3] == board[6] != ' ':  
    return board[0]
  elif board[1] == board[4] == board[7] != ' ':
    return board[1]
  elif board[2] == board[5] == board[8] != ' ':
    return board[2]

  # check diagonals
  elif board[0] == board[4] == board[8] != ' ':
    return board[0]
  elif board[2] == board[4] == board[6] != ' ':
    return board[2]

  # check if draw
  if ' ' not in board:
    return 'draw'

  return None

print("Welcome to Tic Tac Toe!")

while True:
  print_board()
  player_move('X')  
  result = check_win()
  if result != None:
    print(result, "won!") 
    break

  print_board()
  player_move('O')
  result = check_win()
  if result != None:
    print(result, "won!")
    break
