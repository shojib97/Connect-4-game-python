import time
import random
import os
import sys


class Player:
        def __init__(self, letter, board):
                self.symbol = letter # Store reference to the symbol
                self.gboard = board  # store a reference to the board 
        
        def get_player_symbol(self):
                return self.symbol# this function returns the symbol
                
class HumanPlayer(Player):
        def __init__(self, letter, board):
                Player.__init__(self, letter, board)  
                
        def play(self):# the function allow the user to input the column number based on the status of free.
                free = False #by default free is set as False
                row = 0
                while (free == False): # this while loop will keep on going if free is assigned to False.
                        try:
                                print("Human Player %s turn" %self.get_player_symbol())# it will print this message with the human player symbol.
                                c = input("Enter Column No : or press r to restart the game")# this message will invite the player to put the input of the column number.
                                if c.lower().startswith('r'):# if the user types anything that starts with "r" it will run the function below
                                       self.restart_game()# this function will be ran,if the user types anything that starts with "r".
                                if not c.isdigit():# if the input c is a number it will continue
                                        continue
                                c = int(c)# and it will convert the input into and integer
                                for i in range(self.gboard.get_row()-1,-1,-1):# this for loop allow the user to check if the row contains a symbol
                                        row = i                        
                                        free = self.gboard.is_space_free(row, c)# given the column and row, checks if there is a symbol 
                                        if free == True: #if is free it will break the while loop. 
                                                break
                        except (IndexError): #This try and except function is used to prevent the user to input a number out of range.
                                print("Please Enter the coloumns between 0-%d" %(self.gboard.get_coloumns()-1))
                self.gboard.make_move(row, c, self.get_player_symbol())# Then, it will make the move by putting the symbol in the column starting from the bottom.

        def restart_game(self):
                from main import Main
                main = Main() # this function returns main
                return main
               

                

class ComputerPlayer(Player):
        def __init__(self, letter, board):
                Player.__init__(self, letter, board) 
                
        def play(self):
                free = False # the function allow the user to input the column number based on the status of free
                while (free == False): #this while loop will keep on going if free is assigned to False.
                        print("ComputerPlayer %s turn" %self.get_player_symbol()) # it will print this message with the computer player symbol.
                        time.sleep(2) #the computer is thinking for 2 seconds
                        c = random.randint(0, (self.gboard.get_coloumns()-1))# it will chose a random number between 0 and the number of columns subtracted with 1
                        for i in range(self.gboard.get_row()-1,-1,-1): # this for loop allow the user to check if the row contains a symbol
                                row = i                           
                                free = self.gboard.is_space_free(row, c)# given the column and row, checks if there is a symbol
                                if free == True: #if is free it will break the while loop
                                        break
                self.gboard.make_move(row, c, self.get_player_symbol())# Then, it will make the move by putting the symbol in the column starting from the bottom.
                
                
        def restart_game(self):
                return False
        
class HumanPlayer2(Player):
        def __init__(self, letter, board):
                Player.__init__(self, letter, board)  
                
        def play(self):
                free = False #by default free is set as False
                row = 0
                while (free == False): # this while loop will keep on going if free is assigned to False.
                        try:
                                print("Human Player %s turn" %self.get_player_symbol()) # it will print this message with the human player symbol.
                                c = input("Enter Column No : or press r to restart the game ")# this message will invite the player to put the input of the column number.
                                if c.lower().startswith('r'):# if the user types anything that starts with "r" it will run the function below
                                       self.restart_game()# this function will be ran,if the user types anything that starts with "r".
                                if not c.isdigit():# if the input c is a number it will continue
                                        continue
                                c = int(c)# and it will convert the input into and integer
                                for i in range(self.gboard.get_row()-1,-1,-1):# this for loop allow the user to check if the row contains a symbol
                                        row = i                        
                                        free = self.gboard.is_space_free(row, c)# given the column and row, checks if there is a symbol 
                                        if free == True: #if is free it will break the while loop. 
                                                break
                        except (IndexError): #This try and except function is used to prevent the user to input a number out of range.
                                print("Please Enter the coloumns between 0-%d" %(self.gboard.get_coloumns()-1))
                self.gboard.make_move(row, c, self.get_player_symbol())# Then, it will make the move by putting the symbol in the column starting from the bottom.
                
        def restart_game(self):
                from main import Main
                main = Main()# this function returns main
                return main
                                
class ComputerPlayer2(Player):
        def __init__(self, letter, board):
                Player.__init__(self, letter, board) 
                
        def play(self):
                free = False# the function allow the user to input the column number based on the status of free
                while (free == False): #this while loop will keep on going if free is assigned to False.
                        print("ComputerPlayer %s turn" %self.get_player_symbol()) # it will print this message with the computer player symbol.
                        time.sleep(2) #the computer is thinking for 2 seconds
                        c = random.randint(0, (self.gboard.get_coloumns()-1))# it will chose a random number between 0 and the number of columns subtracted with 1
                        for i in range(self.gboard.get_row()-1,-1,-1): # this for loop allow the user to check if the row contains a symbol
                                row = i                         
                                free = self.gboard.is_space_free(row, c) # given the column and row, checks if there is a symbol
                                if free == True: #if is free it will break the while loop
                                        break
                self.gboard.make_move(row, c, self.get_player_symbol()) # Then, it will make the move by putting the symbol in the column starting from the bottom.
                
        def restart_game(self):
                return False
