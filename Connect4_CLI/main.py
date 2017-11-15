from gameboard import GameBoard
from player import HumanPlayer
from player import ComputerPlayer
from player import HumanPlayer2
from player import ComputerPlayer2

class Main:
        def __init__(self):
                pass


        def main():
                print("Welome to connect 4 game \n") #Welcome message.
                print("Please enter the number of rows of the gameboard") # This message will ask the user to input the number of rows.
                row = int(input()) # This input allows the user to input the number of rows.
                valid = True # By default valid is true.
                while (valid == True): #The while loop is used make sure that the user inputs the correct number of rows.
                        try:
                                if int(row) <=4: # This if statement makes sure that the user inputs more than 4 in the number of rows.
                                        while(int(row) <=4):
                                                print("Please enter a valid number of rows(5 or more) ")# if the user enters an invalid number of rows, this message will come up telling them that they should enter a valid number of rows.
                                                row = int(input()) # this input will be used until the user does not input the correct number of rows, thanks to the while loop.
                                else:
                                        break # if the user inputs the correct value in number of rows, the program will continue.
                        except (ValueError):# Try and except is used to avoid the user inputting string instead of numbers.
                                print("Please input a number not a string")
                                row = int(input())

                print("Please enter the number of coloumns of the gameboard")# This message will ask the user to input the number of coloumns.
                col = int(input()) # This input allows the user to input the number of coloumns.
                valid = True #By default valid is true.
                while (valid == True): #The while loop is used make sure that the user inputs the correct number of coloumns.
                        try:
                                if int(col) <=4: #This if statement makes sure that the user inputs more than 4 in the number of coloumns.
                                        while(int(col) <=4):
                                                print("Please enter a valid number of columns(5 or more) ") # if the user enters an invalid number of coloumns, this message will come up telling them that they should enter a valid number of coloumns.
                                                col = int(input()) #this input will be used until the user does not input the correct number of coloumns, thanks to the while loop.
                                else:
                                        break # if the user inputs the correct value in number of coloumns, the program will continue
                        except ValueError: # Try and except is used to avoid the user inputting string instead of numbers.
                                print("Please input a number not a string")
                                col = int(input())


        
                print("Please choose colour for Player 1") # This message will appear in order to ask the user to choose the colour for player 1.
                symbol1= input().upper() # this input will allow the user to input the colour for Player 1. (.upper is used, so that the letter of the colour is always a Capital Letter.)
                while not (symbol1.isalpha() and len(symbol1) == 1): # this while loop is used to allow the user to input only letter(using .isalpha) with lenght as 1.
                        print("Please choose a Valid colour for Player 1!!!")# This message will appear every time the user input an invalid colour for Player 1.
                        symbol1= input().upper() #this input will be used until the user does not input a valid colour for Player1, thanks to the while loop.
                
                print("Please Choose colour for Player 2")# This message will appear in order to ask the user to choose the colour for player 2.
                symbol2= input().upper()# this input will allow the user to input the colour for Player 2. (.upper is used, so that the letter of the colour is always a Capital Letter).
                while not (symbol2.isalpha()and len(symbol2) == 1 and symbol2 != symbol1):# this while loop is used to allow the user to input only letter(using .isalpha).
                        print("Please choose a Valid colour for Player 2!!!")# This message will appear every time the user input an invalid colour for Player 2 with lenght as 1. it will also avoid that the letter used in symbol1 is same as the letter used in symbol2
                        symbol2= input().upper()#this input will be used until the user does not input a valid colour for Player1, thanks to the while loop.
                

                print("Please choose \n 1.Human Player vs Computer Player\n 2.Human Player vs Human Player\n 3.Computer Player vs Computer Player")# This message will appear in order to ask the user to choose the game mode that they want to play.
                try:
                        choice = int(input()) # This input will allows the user to choose the game mode.
                
                except ValueError: # Try and except is used to avoid the user inputting string instead of numbers.
                        print("Please input a number not a string")
                        choice = int(input())
        
                while not(choice <= 3 and choice >= 1): # The while loop is used, so that the user does not enter a number between 1 and 3.
                        try: # Try and except is used to avoid the user inputting string instead of numbers.
                                print("please choose a number from 1-3") #This message will appear if the user inputs a number bigger than 3 in order to remind him/her to choose a number between 1 and 3
                                choice = int(input())# This input will be used until the user does not input a number between 1 and 3
                                if choice <=3 and choice >=1: 
                                        break # if the user enter a number between 1 and 3 the game will continue.
                        except ValueError:
                                print("Please input a number not a string")
                                choice = int(input())
                

                gboard = GameBoard(row,col,symbol1,symbol2)
                p1 = HumanPlayer(symbol1, gboard)   # Create Human player object
                p2 = ComputerPlayer(symbol1, gboard) # Create Computer player object
                p3 = ComputerPlayer2(symbol2, gboard) # Create 2nd Computer player object
                p4 = HumanPlayer2(symbol2, gboard) # Create 2nd Human player object
        
                list1= (p1, p3)# Place HumanPlayer and ComputerPlayer2 in tuple for turn based game.
                list2 = (p1, p4) #Place HumanPlayer and HumanPlayer2 in tuple for turn based game.
                list3 = (p2,p3) # Place ComputerPlayer and Computerplayer2 in tuple for turn based game.
        
                if choice == 1: 
                        players_lst = list1 # if the user chooses 1 the first tuple will be the player list
                elif choice == 2:
                        players_lst = list2 # if the user chooses 2 the second tuple will be the player list
                else:
                        players_lst = list3# if the user chooses 3 the third tuple will be the player list
                
        
                winner = False
                full = False

        
                #gboard.read_game() not working
                gboard.show_board_dynamic() # show empty grid at the beginning of the game
        
                while (winner == False and full == False):
                        # This is to allow players to take turns. 
                        # The game begins with the player at index zero in the tuple,
                        # When the player completes its turn, the next player in the tuple will be asked to play. 
                        # If there is no winner, this continue until reaching the end of the players list, and then we start again
                        # from the beginning of the list.
                
                        for p in players_lst:
                                p.play()
                                gboard.show_board_dynamic() # After each move, the board is shown on the screen
                                winner = gboard.check_winner() # The board will check after each move, if any player has won the game
                                full = gboard.is_board_full() # The board will check after each move, if the gamboard is full

                                if full == True and winner == False:
                                        print("Match drawn")#if the board is full it will declare that the match drawn, therefore there are no winners
                                        print("Do you want to play again? (y or n)")
                                        play_again= input().lower()
                                        if play_again == ('y'):
                                                return main()
                                        break #Terminate game announcing the draw
                        
                                elif winner == True:
                                # Show current player's symbol as Winner, 
                                # and terminate the game
                                        print()
                                        print ("Player %s is the Winner!" % p.get_player_symbol())
                                        print("Do you want to play again? (y or n)")
                                        play_again= input().lower()
                                        if play_again == ('y'):
                                                return main()
                        
                                        break  # end the game and announce the winner.
        #gboard.save_game() not working
        
                                                        
Main.main()          
