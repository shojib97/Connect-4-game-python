class Player:
        def __init__(self, letter):
                self.symbol = letter
        
        def get_player_symbol(self):
                return self.symbol


class HumanPlayer(Player):
    
        def __init__(self, letter):
                Player.__init__(self, letter)      
    
        def play(self):
                # do nothing as the play is done at the Button_GUI
                pass 
        
    
import random
import time
class ComputerPlayer(Player):
    
        def __init__(self, letter, buttns_list):
                Player.__init__(self, letter)
                self.buttons_2d_list = buttns_list
        
        
        def play(self):
                is_space_free = False
                while (is_space_free == False):
                        r = random.randint(0,5)
                        c = random.randint(0,6)
                        self.button = self.buttons_2d_list[r][c]
                        is_space_free = self.button["text"] == " "
                self.button.invoke()
