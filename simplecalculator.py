from interface import UI
from utils.settings import Settings
from calculator import Calculator

class SimpleCalculator:
    """ Main class """

    def __init__(self):
        """ Initializes program """

        self.settings = Settings()

        self.calc = Calculator(self.settings)
        
        
        self.ui = UI(self)

    def run_calculator(self):
        """ Starts the program """

        self.ui.run_ui()
        



if __name__ == "__main__":
    calculator = SimpleCalculator()
    calculator.run_calculator()