#global variables

game_still_going=True
winner=None
current_player="X"

#game board

game_board=['-','-','-',
            '-','-','-',
            '-','-','-']

def display_board():
    print(game_board[0]+"|"+game_board[1]+"|"+game_board[2])
    print(game_board[3]+"|"+game_board[4]+"|"+game_board[5])
    print(game_board[6]+"|"+game_board[7]+"|"+game_board[8])

def play_game():
  global winner 
  display_board()
  while game_still_going:
    placing_input()
    check_if_game_over()
    flip_player()


  if winner=="X" or winner=="O":
    print(winner+" wins")
  elif winner==None:
    print("tie")


def placing_input():
  global current_player
  print(current_player+"'s turn")
  position_var=input("choose a position from 1-9: ")

  while position_var not in ['1','2','3','4','5','6','7','8','9']:
    print("please enter a right position")
    position_var=input("choose a position from 1-9: ")

  while game_board[(int(position_var)-1)] != "-":
    print("please enter a right position")
    position_var=input("choose a position from 1-9: ")


  
  position_var =int(position_var) -1
  game_board[position_var]=current_player
  display_board()
    
def check_if_game_over():
  check_win()
  check_tie()
  return


def check_win():
  global winner
  row_winner=check_row()
  column_winner=check_column()
  diagonal_winner=check_diagonal()

  if row_winner:
    winner=row_winner
  elif column_winner:
    winner=column_winner
  elif diagonal_winner:
    winner=diagonal_winner

def check_row():
  global game_still_going
  row1=game_board[0]==game_board[1]==game_board[2]!='-'
  row2=game_board[3]==game_board[4]==game_board[5]!='-'
  row3=game_board[6]==game_board[7]==game_board[8]!='-'
  if row1 or row2 or row3:
    game_still_going=False
  if row1:
    return game_board[1]
  elif row2:
    return game_board[3]
  elif row3:
    return game_board[6]
  return




def check_column():
  global game_still_going
  column1=game_board[0]==game_board[3]==game_board[6]!='-'
  column2=game_board[1]==game_board[4]==game_board[7]!='-'
  column3=game_board[2]==game_board[5]==game_board[8]!='-'
  if column1 or column2 or column3:
    game_still_going=False

  if column1:
    return game_board[0]
  elif column2:
    return game_board[1]
  elif column3:
    return game_board[2]
  return

def check_diagonal():
  global game_still_going
  diagonal1=game_board[0]==game_board[4]==game_board[8]!='-'
  diagonal2=game_board[2]==game_board[4]==game_board[6]!='-'
  if diagonal1 or diagonal2:
    game_still_going=False

  if diagonal1:
    return game_board[0]
  elif diagonal2:
    return game_board[2]  
  return

    
def check_tie():
  global game_still_going
  if "-" not in game_board:
    game_still_going=False

  return

def flip_player():
  global current_player
  if current_player=="X":
    current_player="O"
  elif current_player=="O":
    current_player="X"
  return

play_game()

