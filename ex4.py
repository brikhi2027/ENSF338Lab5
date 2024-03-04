#    1. Implement a queue which internally uses Python arrays. enqueue()
#    must insert an element at the head, and dequeue() must remove an
#    element from the tail [0.3 pts]

class Arrays:
    def __init__(self, capacity):
        self._array = [None for i in range(0, capacity)]
        self._head = -1
        self._tail = -1
        self.capacity = capacity

    def enqueue(self, value):
        if self._head == -1: # checks if inserting first element
            self._head += 1
            self._tail += 1
            self._array[self._tail] = value
        elif self._tail == (self.capacity - 1): # checks if full
            print("Queue is full")
            return
        else:
            self._tail += 1
            self._array[self._tail] = value

    def dequeue(self):
        if self._head == -1: # checks if empty
            print("Can't delete from an empty queue")
            return
        elif self._tail == 0: # checks if dequeuing last element
            self._head = -1
            self._tail = -1
        else:
            for i in range(0, self._tail):
                self._array[i] = self._array[i+1]
            self._tail -= 1
    
    def print(self):
        if self.capacity == 0:
            print("[]")
        else:
            arr = []
            for i in range(0, self._tail + 1):
                arr.append(self._array[i])
            print(arr)


