class Display:

    @classmethod
    def inputHandler(cls, displayText, input):
        if (type(input) is int):    return cls._numberHandler(displayText, str(input))
        if (input == '.'):  return cls._dotHandler(displayText)

    @staticmethod    
    def _numberHandler(displayText, number):
        if displayText == '0' or displayText.lower() == 'nan':
            return number
        else:   return displayText + number

    @classmethod
    def _dotHandler(cls, displayText):
        if ('.' in displayText):    return displayText
        if (cls.isNaN(displayText)): return '0.'
        else:   return displayText + '.'

    @classmethod
    def delHandler(cls, displayText):
        if cls.isNaN(displayText) or len(displayText) == 1:
            return '0'
        else:   return displayText[:-1]

    @staticmethod
    def isNaN(inputText):
        return (inputText.lower() == 'nan')
