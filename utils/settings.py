
class Settings:
    """ class to hold ui settings """

    def __init__(self):
        
        # Button settings
        self.button_height = 30
        self.button_width = 60
        self.button_weight = 1
        # nr buttons across
        self.nr_buttons_side = 4

        # Root window settings
        self.main_height = '230'
        self.main_width = '275'

        self.main_geometry = str(self.main_width) + "x" + self.main_height
        
        # Frame settings
        self.display_frame_weight = 1
        self.button_frame_weight = 4

        # Calculator stuff
        self.operators = ["+", "-", "*", "/"]

