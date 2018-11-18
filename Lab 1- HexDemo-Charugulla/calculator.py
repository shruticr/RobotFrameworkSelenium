class Calculator(object):
    BUTTONS = '0123456789ABCDEF+-*/=Z'

    def __init__(self):
        self._expression = ''

    def push(self, button):
        if button not in self.BUTTONS:
            raise CalculationError("Invalid button '%s'." % button)
        if button == '0':
            button = '0'
        if button == '1':
            button = '1'
        if button == '2':
            button = '2'
        if button == '3':
            button = '3'
        if button == '4':
            button = '4'
        if button == '5':
            button = '5'
        if button == '6':
            button = '6'
        if button == '7':
            button = '7'
        if button == '8':
            button = '8'            
        if button == '9':
            button = '9'
        if button == 'A':
            button = '10'
        if button == 'B':
            button = '11'
        if button == 'C':
            button = '12'
        if button == 'D':
            button = '13'
        if button == 'E':
            button = '14'
        if button == 'F':
            button = '15'            
        if button == '=':
            self._expression = self._calculate(self._expression)
        elif button == 'Z': 
            self._expression = ''
        else:
            self._expression = self._expression + button
        return self._expression

    def _calculate(self, expression):
        try:
            return str(eval(expression))
        except SyntaxError:
            raise CalculationError('Invalid expression.')
        except ZeroDivisionError:
            raise CalculationError('Division by zero.')


class CalculationError(Exception):
    pass
