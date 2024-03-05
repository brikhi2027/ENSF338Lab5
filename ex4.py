#    1. Implement a queue which internally uses Python arrays. enqueue()
#    must insert an element at the head, and dequeue() must remove an
#    element from the tail [0.3 pts]

class QueueArrays:
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

# 2. Implement a queue which internally uses a singly-linked list.
# enqueue() must add an element at the head, and dequeue() must
# remove the tail element (make sure to keep a tail pointer!) [0.3 pts]

class Node:
    def __init__(self, data, next):
        self._data = data
        self._next = next
    def getData(self):
        return self._data
    def setData(self, data):
        self._data = data
    def getNext(self):
        return self._next
    def setNext(self, next):
        self._next = next
    def toString(self):
        return str(self._data)

class QueueLinkedLists:
    def __init__(self):
        self._head = None
        self._tail = None

    def enqueue(self, value):
        if self._head == None: # if inserting to empty list
            self._head = Node(value, None)
            self._tail = self._head
            return
        else:
            new_node = Node(value, None)
            current = self._tail
            current.setNext(new_node)
            self._tail = current.getNext()

    def dequeue(self):
        if self._head == None:
            print("Can't dequeue from an empty list")
            return
        elif self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            delete = self._head
            self._head = self._head.getNext()
            delete._next = None
            delete = None

    def print(self):
        current = self._head
        while current is not None:
            print(current.toString())
            current = current.getNext()

# 3. Write a function which generates random lists of 10000 tasks. Each
# task is either an enqueue w/ probability 0.7, or a dequeue w/
# probability 0.3 [0.3 pts]

import numpy as np
import random

def generate_list():
    operations = ['enqueue', 'dequeue']
    weights = [0.7, 0.3]

    list = np.random.choice(operations, 10, p=weights)
    full_list = []
    for i in range(0, len(list)):
        operation_type = list[i]
        full_operation = list[i] + '(' + str(random.randint(0, 10)) + ')'
        full_list.append(full_operation)
    return full_list

# 4. Measure the performance of both implementations on 100 such
# lists of tasks using timeit and print the results [0.3 pts]

import timeit

def arraysPerformance(arr, task_list):
    time = 0
    
    for operation in task_list:
        num = ''
        for x in operation:
                if x.isdigit():
                    num += x
        num = int(num)

        if 'enqueue' in operation:
            time += timeit.timeit(lambda: arr_enqueue(arr,x), number = 1)
        else:
            time += timeit.timeit(lambda: arr_dequeue(arr), number = 1)

    return time

def arr_enqueue(arr,x):
    arr.enqueue(x)

def arr_dequeue(arr):
    arr.dequeue()



def linkedListsPerformance(list, task_list):
    time = 0
    for operation in task_list:
            op = 'list.' + operation
            time += timeit.timeit(stmt=op,number=1)
    return time


# 5. Plot the distribution of times (distributions for each implementation
# should be overlayed in the same plot; make sure to use consistent
# ranges) and discuss the results [0.3 pts]

array_times = []
linkedlist_times = []

for i in range(100):
    tasks = generate_list()
    array_queue = QueueArrays(10000)
    list_queue = QueueLinkedLists
    array_times.append(arraysPerformance(array_queue, tasks))
    linkedlist_times.append(linkedListsPerformance(list_queue, tasks))
array_avgtime = sum(array_times) / 100
list_avgtime = sum(linkedlist_times) / 100

print('Average time for array stack implementation:', array_avgtime, 'seconds.')
print('Average time for linked list stack implementation:', list_avgtime, 'seconds.')
