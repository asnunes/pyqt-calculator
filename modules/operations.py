class OperationHandler:

    ADD_OP = 'add'
    SUBTRACT_OP = 'subtract'
    MULTIPLY_OP = 'multiply'
    DIVIDE_OP = 'divide'

    def __init__(self):
        self.prevNumber = None
        self.operationType = None

    def setNewOperation(self, prevNumber, operationType):
        self.prevNumber = prevNumber
        self.operationType = operationType

    def operate(self, nextNumber):
        if self.isDefined():
            operation = getattr(self, self.operationType)
            return operation(self.prevNumber, nextNumber)
        else:
            return nextNumber

    def isDefined(self):
        return not (self.prevNumber is None or self.operationType is None)

    @staticmethod
    def add(prevNumber, nextNumber):
        return prevNumber + nextNumber
    
    @staticmethod
    def subtract(prevNumber, nextNumber):
        return prevNumber - nextNumber

    @staticmethod
    def multiply(prevNumber, nextNumber):
        return prevNumber * nextNumber

    @staticmethod
    def divide(prevNumber, nextNumber):
        if nextNumber == 0: return float('NaN')
        else:   return prevNumber / nextNumber
