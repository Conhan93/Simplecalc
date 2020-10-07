
class Settings:
    """ class to hold ui settings """

    def __init__(self):
        
        self.button_height = 30
        self.button_width = 60

        # Root window settings
        self.main_height = '300'
        self.main_width = '270'

        self.main_geometry = str(self.main_width) + "x" + self.main_height

        self.display_frame_weight = 1
        self.button_frame_weight = 4

        # Button settings
        self.button_height = 30
        self.button_width = 60
        self.button_weight = 1


        # Calculator stuff
        self.operators = ["+", "-", "*", "/"]

