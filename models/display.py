class Display:

    @classmethod
    def inputHandler(cls, displayText, input):
        if (type(input) is int):
            return cls._numberHandler(displayText, str(input))
        if (input == '.'):
            return cls._dotHandler(displayText)

    @staticmethod    
    def _numberHandler(displayText, number):
        return displayText + number

    @staticmethod
    def _dotHandler(displayText):
        if ('.' in displayText):
            return displayText
        else:
            return displayText + '.'