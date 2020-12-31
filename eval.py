
class Evaluator:
    """ Class to evaluate expressions """

    def __init__(self, settings):

        self.operators = settings.operators

        #self.calc_stack = []
    
    def evaluate(self, arguments):

        return self._calculate_result(arguments)

    def _calculate_result(self, arguments):
     
        calc_stack = []
        # if token is parentheses(in list)
        for index,token in enumerate(arguments):
            if type(token) == list:
                arguments.insert(index, self._calculate_result(token))
                arguments.remove(token)

        for operator in self.operators:
            while operator in arguments:
                for index, argument in enumerate(arguments):
                    if argument == operator:
                        calc_stack.append(arguments[index-1])
                        calc_stack.append(arguments[index+1])
                        self._perform_operation(argument, calc_stack)

                        # removes two tokens and replaces the third with result
                        for i in range(2):
                            arguments.pop(index-1)
                        if(len(arguments) >= 3):
                            arguments[index-1] = calc_stack.pop()

        # return value of expression         
        return float(calc_stack.pop())

    def _is_operator(self, item):
        return item in self.operators
    
    def _perform_operation(self, argument, calc_stack):
        """ performs current operation """
        last, first = float(calc_stack.pop()), float(calc_stack.pop())

        if argument == '+':
            calc_stack.append(first + last)
        elif argument == '-':
            calc_stack.append(first - last)
        elif argument == '*':
            calc_stack.append(first * last)
        elif argument == '/':
            calc_stack.append(first / last)
        elif argument == '^':
            calc_stack.append(first ** last)
        