from _parser import Parser 
from eval import Evaluator

class Calculator:
    """ The class that does all the calculations """

    def __init__(self, settings):
        """ The class that does all the calculations """

        
        self.settings = settings

        # stuff that does the actual work
        self.parser = Parser(settings)
        self.evaluator = Evaluator(settings)

        # Result that will be displayed
        self.result = 0

        # input 
        self.input = ""

        # operators
        self.operators = settings.operators

        self.memory_operator = ''

    def calculate(self):
        """ Calculates the result from the input string """
        
        if self.input:
            if self.input.startswith(tuple(self.operators)):
                self.memory_operator = self.input[0]
                self.input = self.input[1:]

            tokens = self.parser.parse(self.input)
            
            if self.memory_operator:
                self.result = self.memory_operation(self.evaluator.evaluate(tokens))
                self.memory_operator = ''
            else:
                self.result = self.evaluator.evaluate(tokens)
  
           
            self.input = ""
    def memory_operation(self, result):
        """ handles operation to stored result """
        tokens = [str(self.result),
                  self.memory_operator,
                  str(result)]
        return self.evaluator.evaluate(tokens)

    def get_result(self):
        """ returns calculated result in string """
        return str(self.result)
    def get_input(self):
        """ returns input string """
        return self.input
    def set_input(self, _input):
        """ concatenates on calculator input string """

        if _input == 'mc':
            self.clear_memory()
            return

        # skips entering an operator if calculator input already ends with an operator
        if list(filter(self.input.endswith, self.settings.operators)):
            if _input in self.settings.operators:
                return

        self.input += _input
    def clear_memory(self):
        """ sets result to 0 """
        self.result = 0


