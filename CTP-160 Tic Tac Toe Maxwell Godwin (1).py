#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Tic Tac Toe game
@Xi Kramer
"""

def display_board(board):
    '''
    print the current board on the screen using a 3 X 3 table representing a Tic tac Toe board
    The presentation giving the users important info to decide their next moves
    :param board: the board (a list) contains current game data
    :return: None

    number 1 - 9 corresponding to the positions on a 3 X 3 table
    _________
    7 | 8 | 9
    4 | 5 | 6
    1 | 2 | 3

    for example:
    __________
    Game Board
      |   |
    x |   |
      | x | o

    '''
    print("__________")
    print("Game Board")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[0]} | {board[1]} | {board[2]}")


def marker_choice():
    '''
    prompt the users which marker they'd like to use for this game ('x' or 'o')
    if player didn't choose 'x', ('0','x') will be assigned
    because this function returns a tuple, make  sure you unpack the tuple when call, example:
    player1_marker, player2_marker = marker_choice()
    :return: a tuple (player1's marker of choice, player2's marker of choice)
    '''
    marker=" "
    while marker != "x" and marker != "o":
        marker=input("player 1, please choose your marker (x or o):")
    player_1=marker
    if player_1 != "x":
        player_2="x"
    else:
        player_2="o"
    return(player_1,player_2)

def place_marker(board, marker, position):  # current board list, which marker, place where
    '''
    takes in the board list, info of which marker and where to place it
    assign to the board - update the list
    :param board: the board (a list) contains current game data
    :param marker: marker choice of the calling player
    :param position: position of the player's choice
    :return: None
    '''
    if board[position-1]==" ":
        board[position-1]=marker 
        
def haswon(board, marker):
    '''
    when the player wins the game?
    when all rows are the same, when all columns are the same, when diagonal lines are the same, and
    exclue the situation when the board is empty, or the whole row is empty, etc...
    it's bit tricky, that's why we have "marker" passed in as a parameter
    can you figure it out?
    :param board: the board (a list) contains current game data
    :param marker: the player's marker whoever is calling the function to check if haswon
    :return: boolean true of false
    '''
    if board:
        if (not " " in board[0:3]) and (board[0]==board[1]==board[2]==marker):
                return True

        if (not " " in board[3:6]) and (board[3]==board[4]==board[5]==marker):
                return True
            
        if (not " " in board[6:9]) and (board[6]==board[7]==board[8]==marker):
                return True
            
        if (not " " in (board[0],board[4],board[8])) and (board[0]==board[4]==board[8]==marker):
                return True
            
        if (not " " in (board[6],board[4],board[2])) and (board[6]==board[4]==board[2]==marker):
                return True
            
        if (not " " in (board[0],board[3],board[6])) and (board[0]==board[3]==board[6]==marker):
                return True   
            
        if (not " " in (board[1],board[4],board[7])) and (board[1]==board[4]==board[7]==marker):
                return True          
            
        if (not " " in (board[2],board[5],board[8])) and (board[2]==board[5]==board[8]==marker):
                return True          
        
        else:
            return False 

def choose_first():
    '''
    use random.randint function to generate a random number to decide which player goes first
    player 1 has a chance to choose preferred marker, but computer decides which player goes first
    you need to import the random library
    :return: a string 'player 1" or 'player 2'
    '''
    import random 
    num=random.randint(0,1)
    if num==0:
        return "player 1"
    else:
        return "player 2"

def board_isfull(board):
    '''
    a helpful function
    if the board is full, the game should stop
    if the board is full, the program should not call player_choice to get a posistion
    traverse the board to see if it is full
    :param board: the board (a list) contains current game data
    :return: boolean true of false
    '''
    if board.count(" ") > 1 :
        return False 
    else:
        return True
    
def player_choice(board):
    '''
    prompt the user to make a choice where they would like to go next
    note: check if the board if full first, then call this function to get a choice
    if the board is full then what do you tell the user?
    :param board:
    :return: an integer representing a position
    '''
    if board_isfull(board):
        print("The board is full")
    else:
        return get_digit(board)

def get_digit(board):
    '''
    optional helper function"  get an input then convert to a digit
     better: make sure it's a digit and a valid digit for this game: 1-9
    :return: a digit
    '''
    step=int(input("Where do you want to make your next move?"))
    if board[step -1] == " " and 1<step<9:
        return step
    else: 
        while board[step - 1] != " " or step>9 or step <1:
            step=int(input("You can not choose that position. Where do you want to make your next move?"))
        return step

def replay():
    '''
    prompt the user if wish to play the game again
    optional: friendly accept uppercase or lowercase
    :return: boolean true or false
    '''
    again=" "
    while again.lower() != "yes" and again.lower() != "no":
        again=input("Do you want to play the game again? (please reply yes or no)")
    if again.lower() == 'yes':
        return True
    else:
        return False 
    
def yes_no():
    '''
    helper function
    get input from the players
    return boolean True if yes, else return False
    '''
    again=" "
    while again.lower() != "yes" and again.lower() != "no":
        again=input("(please reply yes or no):")
    if again.lower() == 'yes':
        return True
    else:
        return False 

def winning_message(winner):
    '''
    display the winner
    feel free to add designs along with the message
    :param winner: string
    :return: None
    '''
    print(f"{winner}, CONGRATULATIONS YOU WON!!!")
    
def display_keypad():
    '''
    helper function when display instructions
    feel free to modify
    :return: None
    '''
    print("_________")
    print("7 | 8 | 9")
    print("4 | 5 | 6")
    print("1 | 2 | 3")

def instructions():
    '''
    print basic game instructions
    feel free to modify
    :return: None
    '''
    print("This is a two-player game. Each player takes turns and")
    print("choose a corresponding position of where you'd place")
    print("your marker according to the following keypad layout:")
    display_keypad()

def play_TicTacToe():
    '''
    The main controller
    Do not modify this function in order to earn full credits of this project
    You must use this function as the main control to get full credits
    You may modify but must submit as additional versions - just for fun, no credits and for future demostration and teaching
    :return:
    '''
    # print game instructions
    print("    *** Welcome to our Tic Tac Toe game! ***    ")
    instructions()

    while True:  #each iteration is one full game/exit if wish not play again
        print("A few questions before we start!")
        the_board = [' '] * 10

        # set player markers
        player1_marker, player2_marker = marker_choice()  # tuple unpacking
        print("Okay, Player 1's marker is '" + player1_marker + "', player 2's marker is '" + player2_marker + "', and", end=" ")

        # who goes first - randomly decide
        # simulate flip coin which player goes first by calling choose_first() which will return "player 1" or "player 2"
        turn = choose_first()
        print(turn + " will go first!")

        # why need to ask "Ready to play?"
        # we will use a boolean gameon to signify if a game is on
        # when there is a win or tie, gameon will be set to false, wait to see if starts another game
        # as user if ready, confirm, set gameon to true until a win or tie set gamon to false
        print("Ready to play?", end=" ")
        gameon = yes_no()  # boolean control one game, ini here

        # game play
        while gameon:  # unless win or tie
            # -----------------player 1's turn--------------------
            if turn == "player 1":  # could switch on 0, or 1, here to be clear
                # 1, display the board by calling display_board(board)
                display_board(the_board)

                # 2, player choose a position by calling player_choice(board)
                print("Player 1 ('" + player1_marker, end="') ")  # reminder the player's current marker choice, nicer message folowing by " choose a position
                position = player_choice(the_board)

                # 3, place the marker on the position by calling place_marker(board, marker, position)
                place_marker(the_board, player1_marker, position)

                # 4, check if they won, or check if it's a tie, else player 2's turn
                # to check if the player has won, by calling haswon(board, mark)
                # to check if it's a tie, by checking if the board if full, by calling board_isfull(board):
                # no tie and no win? next player's turn
                if haswon(the_board, player1_marker):
                    winning_message("PLAYER 1")
                    display_board(the_board)
                    gameon = False
                elif board_isfull(the_board):
                    print("TIE GAME")
                    display_board(the_board)
                    gameon = False
                else:
                    turn = "player 2"
            # --------------------player 2's turn-------------------
            else:  # player 2's turn
                # 1, display the board by calling display_board(board)
                display_board(the_board)

                # 2, player choose a position by calling player_choice(board)
                print("Player 2 ('" + player2_marker, end="') ")
                # print("Player 2", end = " ")
                position = player_choice(the_board)

                # 3, place the marker on the position by calling place_marker(board, marker, position)
                place_marker(the_board, player2_marker, position)  ####change here!

                # 4, check if they won, or check if it's a tie, else player 2's turn
                # to check if the player has won, by calling haswon(board, mark)
                # to check if it's a tie, by checking if the board if full, by calling board_isfull(board):
                # no tie and no win? next player's turn
                if haswon(the_board, player2_marker):  ####change here!
                    winning_message("PLAYER 2")
                    display_board(the_board)
                    gameon = False
                elif board_isfull(the_board):
                    print("Tie game")
                    display_board(the_board)
                    gameon = False
                else:
                    turn = "player 1"  ####change here!
        # --------------------------------
        # single exit the game
        # break out of the while loop on replay()
        print("\nWould you like to play again? ", end=" ")
        if not yes_no():
            print("Thank you. :) Goodbye!")
            break #end the program

    # end while loop

# ----------------------------------
def main():
    play_TicTacToe()

if __name__ == "__main__":
    main()


# 

# In[ ]:





# In[ ]:




