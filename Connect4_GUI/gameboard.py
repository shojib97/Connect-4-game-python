class GameBoard:
        
        def __init__(self, height, width,firstsymbol,secondsymbol):
                        self.__space = ' '
                        self.__row = height #Store reference for row
                        self.__col = width #Store reference for coloumns
                        self.__board = [] #the board is put in to a list
                        self.symbol1 = firstsymbol #Store reference for the first symbol
                        self.symbol2 = secondsymbol #Store reference for the second symbol
                        
                        
                        for i in range (self.__row):
                                row = [' ']*self.__col
                                self.__board.append(row)
                        
        def read_game(self):
                file = open("Games.txt", "r") # Open a file Games.txt in red mode
                for r in range (3):			  # Loop 3 tiles to read all lines in the file Games.txt
                        line = file.readline()	  # At each iteration, read a single line from the file Games.
                        self.__board[r][0] = line[0]	  # Each line is a list of characters. Take first character and put it at column 0 of the row
                        self.__board[r][1] = line[1]	  # Take the second character and put it at column 1 of the row
                        self.__board[r][2] = line[2]	  # Take the third character and put it at column 2 of the row
                        self.__board[r][3] = line[3]	  # Take the fourth character and put it at column 3 of the row

                file.close()                  # close the file

        def save_game(self):
                file = open("Games.txt", "w") #Open a file Games.txt in write mode
                file.write(str(self.__row))#writes the number of rows as string into the text file.
                file.write("\n")
                file.write(str(self.__col))#writes the number of columns as string into the text file.
                file.write("\n")
                file.write(str(self.symbol1))#writes the symbol of the first player as string into the text file.
                file.write("\n")
                file.write(str(self.symbol2))#writes the symbol of the second player as string into the text file
                for x in range(self.__row):
                        for y in range(self.__col):
                                file.write(str(self.__board))

                file.close()
                
        def get_row(self):
                return self.__row # the function returns the number of row

        def get_coloumns(self):
                return self.__col # the functiom returns the number of columns
                                                       
        def make_move(self, row, col, element):
                self.__board[row][col] = element #this function allow the user to make move.
                
                
        def check_winner(self):
        # Given a board and a player's letter, this function returns True if  player has won.
                winner = (self.check_hz() or self.check_vt() or # check the rows and coloumns
                self.check_bottom_left_to_top_right_corner()or # check diagonal row top right to bottom left
                self.check_bottom_right_to_top_left_corner())# check diagonal row top left to bottom right
                # when performing the check, and if there are three elements are equal, then make sure they are not equal to empty space ' ' which is what the 2D array was populated with at the start of the application
                return winner
                
        def check_hz(self):
                #this function check if there are 4 symbol together in the same row.
                row = ''#starts with row as nothing
                for x in range(self.__row):
                        for y in range(self.__col):
                                row += self.__board[x][y] 
                                
                        if self.symbol1 * 4 in row or self.symbol2 *4 in row: #Given the board, it will check if 4 symbol1 or 4 symbol2 are in the same row.
                                return True # it will return True if there are 4 symbol together in the same row.
                        row = ''
                return False # it will return false if there are not 4 symbol together not the same row.
        
        def check_vt(self):
                #this function check if there are 4 symbol together in the same column.
                col = '' #starts with col as nothing
                for y in range(self.__col):
                        for x in range(self.__row):
                                col += self.__board[x][y]
                                
                        if self.symbol1 * 4 in col or self.symbol2 *4 in col: #Given the board, it will check if 4 symbol1 or 4 symbol2 are in the same columns.
                                return True # it will return True if there are 4 symbol together in the same column.
                        col = ''
                return False # it will return false if there are not 4 symbol together not the same columns.

        def check_bottom_left_to_top_right_corner(self):
                #Given the board it will check if there are 4 symbols diagonally together from bottom left to top right corner.
                for x in range(self.__row - 3):
                        for y in range(3, self.__col):
                                p1_diag = self.__board[x][y] == self.symbol1 and self.__board[x + 1][y - 1] == self.symbol1 and self.__board[x + 2][ y - 2] == self.symbol1 and self.__board[x + 3][y - 3] == self.symbol1
                                p2_diag = self.__board[x][y] == self.symbol2 and self.__board[x + 1][y - 1] == self.symbol2 and self.__board[x + 2][ y - 2] == self.symbol2 and self.__board[x + 3][y - 3] == self.symbol2

                                if p1_diag or p2_diag :
                                        return True #it will return True if there are 4 symbol1 or 4 symbol 2 together ina diagonal starting from bottom left to top right corner.

                return False  #it will return False if there are no symbols together in a diagonal starting from bottom left to top right corner.

        def check_bottom_right_to_top_left_corner(self):
                #Given the board it will check if there are 4 symbols diagonally together from bottom right to top left corner.
                for x in range(self.__row - 3):
                        for y in range(self.__col - 3):
                                p1_diag = self.__board[x][y] == self.symbol1 and self.__board[x + 1][y + 1] == self.symbol1 and self.__board[x + 2][ y + 2] == self.symbol1 and self.__board[x + 3][y + 3] == self.symbol1
                                p2_diag = self.__board[x][y] == self.symbol2 and self.__board[x + 1][y + 1] == self.symbol2 and self.__board[x + 2][ y + 2] == self.symbol2 and self.__board[x + 3][y + 3] == self.symbol2

                                if p1_diag or p2_diag:
                                        return True #it will return True if there are 4 symbol1 or 4 symbol 2 together ina diagonal starting from bottom right to top left corner.
                return False #it will return False if there are no symbols together in a diagonal starting from bottom right to top left corner.
        
        
        def is_board_full(self):
                for x in range(self.__row):
                        for y in range (self.__col):
                                if self.__board[x][y] ==' ':#Given the board, it will check if the board contains symbols.
                                        return False #if the board has free spaces, it will return False.
                return True# if the board if full it will return True.
                
        def is_space_free (self, row, col):
                #the functiom contains an if statement to check if the space is free or not.
                if self.__board[row][col] == " ": # if the space is free it will return True, otherwise it will return false.
                        return True
                return False


        def show_board_dynamic(self):
                #this function show the GameBoard dynamically
                print()
                print("-"*(len(self.__board[0])*2+1)) #This allow to print as many as "-" according to the number of columns in the game
                for i in range (len(self.__board)): 
                        for j in range (len(self.__board[0])):
                                print ("|", end = "") #This allow to print as many as "|" according to the number of rows in the game
                                print (self.__board[i][j], end=""),
                        print ("|")
                        print("-"*(len(self.__board[0])*2+1)) #This allow to print as many as "-" according to the number of columns in the game
                        
                print()
                

