class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        return self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if (len(self.stack)) != 0:
            return self.stack[-1]
        else:
            return "Stack is empty"


stack = Stack()


stack.push(5)
stack.push(10)
stack.push(15)
stack.pop()
stack.peek()

