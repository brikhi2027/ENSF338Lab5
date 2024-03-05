#1.
class ArrQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1
    def enqueue(self, element):
        if ((self.tail + 1) % self.capacity) == self.head:
            print('enqueue None')
            return
        elif self.head == -1:
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = element
        print('enqueue', element)
    def dequeue(self):
        if self.head == -1:
            print('dequeue None')
            return
        temp = self.queue[self.head]
        if (self.tail % self.capacity) == self.head:
            self.head = -1
            self.tail = -1
            print('dequeue', temp)
        else:
            self.head = (self.head + 1) % self.capacity
            print('dequeue', temp)
        return temp
    def peek(self):
        if self.head == -1:
            print('peek None')
            return
        else:
            first_element = self.queue[self.head]
        print('peek', first_element)

        
#2. 
class CircularListNode:
    def __init__(self, value):
        self._value = value
        self._next = None
    def getData(self):
        return self._value
    def setData(self, value):
        self._value = value
    def getNext(self):
        return self._next
    def setNext(self, next):
        self._next = next
    def toString(self):
        return str(self._value)

#class ListQueue:
    #def __init__(self):
