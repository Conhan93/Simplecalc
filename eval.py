
class Evaluator:
    """ Class to evaluate expressions """

    def __init__(self, settings):

        self.operators = settings.operators
    
    def evaluate(self, tokens):
        """ handles evaluation sequence """


        return self._calculate_result(tokens)

    def _calculate_result(self, tokens):
        """ calculates result from tokens(tokens) """

        if len(tokens) == 1:
            return float(tokens[0])

        calc_stack = []

        # if token is parentheses(in list)
        for index,token in enumerate(tokens):
            if type(token) == list:
                tokens.insert(index, self._calculate_result(token))
                tokens.remove(token)

        # main loop
        for operator in self.operators:
            while operator in tokens:
                for index, argument in enumerate(tokens):
                    if argument == operator:
                        calc_stack.append(tokens[index-1])
                        calc_stack.append(tokens[index+1])
                        self._perform_operation(argument, calc_stack)

                        # removes two tokens and replaces the third with result
                        for i in range(2):
                            tokens.pop(index-1)
                        if(len(tokens) >= 3):
                            tokens[index-1] = calc_stack.pop()

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
        