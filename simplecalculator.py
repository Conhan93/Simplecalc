from interface import UI
from utils.settings import Settings
from module1 import ActualCalculator

class SimpleCalculator:
    """ Main class """

    def __init__(self):
        """ Initializes program """

        self.actualcalc = ActualCalculator()
        self.settings = Settings()
        
        self.ui = UI(self)

    def run_calculator(self):
        """ main loop of the program """
        while True:
            pass



if __name__ == "__main__":
    calculator = SimpleCalculator()
    calculator.run_calculator()