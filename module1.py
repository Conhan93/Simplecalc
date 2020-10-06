
class ActualCalculator:
    """ The class that does all the calculations """

    def __init__(self):
        """ The class that does all the calculations """

        #self.calculator = calculator

        # Result that will be displayed
        self.result = 0

        # input 
        self.input = ""
        # operators
        self.operators = ["+", "-", "*", "/"]

    def calculate(self):
        if self.input:
            if self.input.startswith("*") or self.input.startswith("/"):
                self.result = eval(str(self.result) + self.input)
            else:
                self.result += eval(self.input)
            print(self.result)
            self.input = ""

    def get_result(self):
        return str(self.result)
    def get_input(self):
        return self.input
    def set_input(self, _input):
        self.input += _input
    def clear_memory(self):
        self.result = 0





"""
An idea to eliminate the need for a seperate function for every type of input
button = Tk.Button(master=frame, text='press', command=lambda: action(someNumber))
worth a try
"""


