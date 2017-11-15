import tkinter

from sys import exit
from tkinter import messagebox
from gameboard import GameBoard
from player import HumanPlayer
from player import ComputerPlayer

        
class GameGUI:
                
        def __init__(self):
                
                self.mw = tkinter.Tk()#creates the main window
                self.row = 6 #sets row as 6
                self.col= 7 #sets columns as 7
                self.buttons_2d_list =  [] #store the gameboard as list.
                for i in range (self.row): 
                        self.coloumns = [' ']*self.col
                        self.buttons_2d_list.append(self.coloumns)
                
                # place players 1 and 2 in tuple for turn based game. 
                self.gboard = GameBoard(self.row,self.col,'X','O')
                p1 = HumanPlayer("X")   
                p2 = ComputerPlayer("O",self.buttons_2d_list)
                
                self.players_lst = (p1, p2)
                self.currnt_player_index = 0
                self.winner = False

        def getrow(self):
                return self.row
        
        def getcol(self):
                return self.col

        def check_coloumns(self,col):
                free = False
                row = self.row - 1
                while row > -1:
                        button = self.buttons_2d_list[row][col]
                        if button["text"] == " ":
                                return row
                        row-=1
                if free == False:
                        return False
                                        
        def clicked_btn(self,x):
        
                p = self.players_lst[self.currnt_player_index]

                c = self.check_coloumns(x)
                if c == False:
                        pass
                
                button = self.buttons_2d_list[c][x] # get the button instance from the list
               
                if button["text"] == " ":
                                                  
                        button["text"] = p.get_player_symbol() # if the button do not contain text it will display the player symbol

                        if p.get_player_symbol() == 'X': # if the player symbol is X, 
                                button["bg"]= "Red" # the button will be coloured as red.
                        else:
                                button["bg"] = "Blue"# otherwise, it will coloured as Blue
                        
                        
                        self.gboard.make_move(c, x, p.get_player_symbol())
                        
                        
                        winner = self.gboard.check_winner() # The board will check after each move, if any player has won the game
                        
                        is_full = self.gboard.is_board_full()
                        
                        if winner == True:
                                # Show current player's symbol as Winner, 
                                        # and terminate the game
                                win_messge = ("Player %s is the Winner!" % p.get_player_symbol())
                                messagebox.showinfo("Winner Info ",win_messge)
                                self.mw.destroy()
                                exit()
                
                        elif is_full == True:
                                messagebox.showinfo("Winner Info", "The game ended in a draw!")# announces draw and terminates the game
                                self.mw.destroy()
                                exit()
                        else:
                                pass
                 
                
                        # change player index to allow the next player to play. 
                        if self.currnt_player_index == 1:
                                self.currnt_player_index = 0
                        else:
                                self.currnt_player_index+=1 # increment index by 1

                        p = self.players_lst[self.currnt_player_index]
                        p.play()
        
        def intialise_dynamic(self):
                #puts the button in a grid
                for x in range(self.row):
                        for y in range(self.col):
                                self.button = tkinter.Button(self.mw, text = " ", font =('Arial 10 bold'), command = lambda  j = y: self.clicked_btn(j),height = 5, width = 10)
                                self.button.grid(row=x,column=y)
                                self.buttons_2d_list[x][y] = self.button

                                
                

                
        
def main():
        b_gui = GameGUI()
        b_gui.intialise_dynamic()
                
                
main()  
