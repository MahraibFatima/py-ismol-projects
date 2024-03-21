import random

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def CheckWin():
  # for player win
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] == "X":
      print("Computer wins.")
      return True
    if board[0][i] == board[1][i] == board[2][i] != "X":
      print("Computer wins.")
      return True
  if board[0][0] == board[1][1] == board[2][2] != "X":
    print("Computer wins.")
    return True
  if board[0][2] == board[1][1] == board[2][0] != "X":
    print("Computer wins.")
    return True
  # for computer win
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] == "O":
      print("Computer wins.")
      return True
    if board[0][i] == board[1][i] == board[2][i] != "O":
      print("Computer wins.")
      return True
  if board[0][0] == board[1][1] == board[2][2] != "O":
    print("Computer wins.")
    return True
  if board[0][2] == board[1][1] == board[2][0] != "O":
    print("Computer wins.")
    return True
  return False


def PrintBoard():
  print("----------")
  print(board[0][0], "|", board[0][1], "|", board[0][2])
  print(board[1][0], "|", board[1][1], "|", board[1][2])
  print(board[2][0], "|", board[2][1], "|", board[2][2])
  print("----------")


def computerTurn():
  if CheckWin():
    return
  while True:
    i = random.randint(0, 2)
    j = random.randint(0, 2)
    # If the cell is empty, place "O" and return
    if board[i][j] == " ":
      board[i][j] = "O"
      return


def resetBoard():
  global board
  board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def checkValid(x):
  if (x < 0 or x > 8):
    print("Invalid input. Please enter a number from 0-8.")
    return False
  if (board[x // 3][x % 3] != " "):
    print("Invalid input. Please enter a number from 0-8.")
    return False
  return True


def takeInput():
  x = int(input("Enter a number to place your X: "))
  if (checkValid(x)):
    board[x // 3][x % 3] = "X"
    PrintBoard()


def play():
  while (True):
    takeInput()
    if (CheckWin()):
      break
    else:
      print("Computer's turn.")
      computerTurn()
      PrintBoard()
    if (CheckWin()):
      resetBoard()
      break