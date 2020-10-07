
class Calculator:
    """ The class that does all the calculations """

    def __init__(self, settings):
        """ The class that does all the calculations """

        #self.calculator = calculator
        self.settings = settings

        # Result that will be displayed
        self.result = 0

        # input 
        self.input = ""
        # operators
        self.operators = settings.operators

    def calculate(self):
        """ Calculates the result from the input string """

        if self.input:
            if self.input.startswith("*") or self.input.startswith("/"):
                self.result = eval(str(self.result) + self.input)
            else:
                self.result += eval(self.input)
            print(self.result)
            self.input = ""

    def get_result(self):
        """ returns calculated result in string """
        return str(self.result)
    def get_input(self):
        """ returns input string """
        return self.input
    def set_input(self, _input):
        """ concatenates on calculator input string """

        # skips entering an operator if calculator input already ends with an operator
        if list(filter(self.input.endswith, self.settings.operators)):
            if _input in self.settings.operators:
                return

        self.input += _input
    def clear_memory(self):
        """ sets result to 0 """
        self.result = 0


