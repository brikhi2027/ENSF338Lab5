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
            #print("Queue is full")
            return
        else:
            self._tail += 1
            self._array[self._tail] = value

    def dequeue(self):
        if self._head == -1: # checks if empty
            #print("Can't delete from an empty queue")
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
            #print("Can't dequeue from an empty list")
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

import random

def generate_list():
    num_enqueue = 0
    num_dequeue = 0
    operations_list = []

    while num_enqueue != 7000:
        op = []
        op.append('enqueue')
        op.append(random.randint(0, 100))
        operations_list.append(op)
        num_enqueue += 1
    while num_dequeue != 3000:
        op = []
        op.append('dequeue')
        operations_list.append(op)
        num_dequeue += 1
    random.shuffle(operations_list)
    return operations_list


# 4. Measure the performance of both implementations on 100 such
# lists of tasks using timeit and print the results [0.3 pts]

import timeit

def arraysPerformance(task_list, arr):
    for operation in task_list:
        if operation[0] == 'enqueue':
            arr.enqueue(operation[1])
        else:
            arr.dequeue()

def linkedListsPerformance(task_list, list):
    for operation in task_list:
        if operation[0] == 'enqueue':
            list.enqueue(operation[1])
        else:
            list.dequeue()

array_time = []
linkedlist_time = []
arrQueueCapacity = random.randint(10000, 15000) #setting a random capacity for the array implementation of queue
for i in range(100):
    tasks = generate_list()
    array_queue = QueueArrays(arrQueueCapacity)
    list_queue = QueueLinkedLists()
    array_time.append(timeit.timeit(lambda: arraysPerformance(tasks, array_queue), number = 1))
    linkedlist_time.append(timeit.timeit(lambda: linkedListsPerformance(tasks, list_queue), number = 1))

array_avgtime = sum(array_time)/100
list_avgtime = sum(linkedlist_time)/100

print('Average time for array queue implementation:', array_avgtime, 'seconds.')
print('Average time for linked list queue implementation:', list_avgtime, 'seconds.')


# 5. Plot the distribution of times (distributions for each implementation
# should be overlayed in the same plot; make sure to use consistent
# ranges) and discuss the results [0.3 pts]
import matplotlib.pyplot as plt

plt.hist(array_time, bins = 10, alpha = 0.8, edgecolor = 'black', label = 'array implementation')
plt.hist(linkedlist_time, bins = 5, color= 'r', alpha = 0.8, label = 'linked list implementation')
plt.legend()
plt.title("Queques")
plt.xlabel('Execution Times')
plt.ylabel('Number of Executions')
plt.xlim()
plt.show()

# The linked list implementation is much faster than the array implementation. This is most likely due
# to the fact that when dequeuing from an array, all elements from index 1 to (n-1) must be shifted over 
# left by one unit, incurring a cost of O(n) every time an element is dequeued. This is because array
# elements can be indexed and so are stored in memory contiguously. Enqueuing is O(1) because a tail
# pointer is implemented and so the index to insert to is known.

# A list's elements are not stored contiguously in memory, which means a list can't be indexed, however,
# a regular queue doesn't require indexing to enqueue or dequeue. This is why in a linked list, 
# even though dequeuing also happens at the head, the rest of the elements do not have to be shifted over,
# so the head pointer is simply updated to point to head.next, which is a complexity of O(1). Enqueuing 
# is also O(1) because a tail pointer was implemented.

# This is why the linked list distribution is around 0s and the array is further right around 0.4s.
