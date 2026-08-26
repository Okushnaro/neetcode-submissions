class MinStack:

    def __init__(self):
        self.stack = list()
        self.minStack = list()
        self.minValue = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minValue is None:
            self.minStack.append(val)
            self.minValue = val
        if self.minValue > val:
            self.minStack.append(val)
            self.minValue = val
        else:
            self.minStack.append(self.minValue)

        
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.minValue = self.minStack[-1]
        if len(self.stack) == 0:
            self.minValue = None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minValue
        
