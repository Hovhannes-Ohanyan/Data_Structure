class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.queue)

queue = Queue()

queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

queue.dequeue()
queue.is_empty()
queue.peek()
queue.size()
