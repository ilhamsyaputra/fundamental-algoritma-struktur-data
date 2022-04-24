class Stack:
    def __init__(self):
        self.data = []

    def read(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]
        
    def push(self, number):
        self.data.append(number)

    def pop(self):
        return self.data.pop()