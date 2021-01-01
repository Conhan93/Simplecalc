
class Parser:
    
    def __init__(self, settings):
        

        self.operators = settings.operators

        # parenthese count - replace with integer?
        self.p_stack = []
        self.last_sub_len = 0

    def parse(self, text):
        stack = []
        last = 0
        
        for index, character in enumerate(text):

            if character == '(' and index >= last:
                self._open_parentheses(stack, text, index, character)
                last = self.last_sub_len + index + 1    

            elif character == ')' and len(self.p_stack) > 0 and index >= last:
                return self._close_parentheses(last, stack, text, index)

            elif character in self.operators and index >= last:
                if text[index-1] not in self.operators and index != 0:
                    stack.append(text[last:index])
                    stack.append(character)
                    last = index + 1

        stack.append(text[last:])
        self._clear_empty_tokens(stack)

        return stack
    def _clear_empty_tokens(self, tokens):
        """ removes empty tokens from list """
        try:
            while True:
                tokens.remove('')
        except:
            pass

    def _close_parentheses(self, last, tokens, text, index):
        """ closes expression inside parentheses, clears empty tokens
            from list, updates last sub len
        """
        self.p_stack.pop()
        tokens.append(tokens.append(text[last:index]))
        tokens.pop()
        self.last_sub_len = index +1
        self._clear_empty_tokens(tokens)
  
        return tokens
    
    def _open_parentheses(self, tokens, text, index, character):
        self.p_stack.append(character)
        tokens.append(self.parse(text[index+1:]))