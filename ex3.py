import random
import timeit
import matplotlib.pyplot as plt
#1. 
class ArrStack:
    def __init__(self):
        self._stack = []
    def push(self, element):
        self._stack.append(element)
    def pop(self):
        if not self._stack:
            return None
        else:
            return self._stack.pop()


#2.
class ListNode:
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

class ListStack:
    def __init__(self):
        self._head = None
    def push(self, value):
        node = ListNode(value)
        node.setNext(self._head)
        self._head = node
    def pop(self):
        if self._head is None:
            return None
        else:
            popped_value = self._head.getData()
            self._head = self._head.getNext()
            return popped_value


#3. 
def random_tasks():
    num_push = 0
    num_pop = 0
    task_list = []

    while num_push != 7000:
        task = []
        task.append('push')
        task.append(random.randint(0, 100))
        task_list.append(task)
        num_push += 1
    while num_pop != 3000:
        task = []
        task.append('pop')
        task_list.append(task)
        num_pop += 1
    
    random.shuffle(task_list)
    return task_list
    
#4. 
def array_performance(task_list, stack):
    for task in task_list:
        if task[0] == 'push':
            stack.push(task[1])
        else:
            stack.pop()

def list_performance(task_list, stack):
    for task in task_list:
        if task[0] == 'push':
            stack.push(task[1])
        else:
            stack.pop()

array_times = []
linkedlist_times = []

for i in range(100):
    tasks = random_tasks()
    array_stack = ArrStack()
    list_stack = ListStack()
    array_times.append(timeit.timeit(lambda: array_performance(tasks, array_stack), number = 1))
    linkedlist_times.append(timeit.timeit(lambda: list_performance(tasks, list_stack), number = 1))
array_avgtime = sum(array_times) / 100
list_avgtime = sum(linkedlist_times) / 100

print('Average time for array stack implementation:', array_avgtime, 'seconds.')
print('Average time for linked list stack implementation:', list_avgtime, 'seconds.')

#5. 
plt.hist(array_times, bins = 10, alpha = 0.8, edgecolor = 'black', label = 'array implementation')
plt.hist(linkedlist_times, bins = 10, alpha = 0.8, edgecolor = 'black', label = 'linked list implementation')
plt.legend()
plt.xlabel('Execution Times')
plt.ylabel('Number of Executions')
plt.ylim(0, 95)
plt.show()

#From the distributions of the array and linked list implementations of a stack, it can be seen that using an array for a stack  
#takes a shorter period of time than using a linked list. The distribution of the array implementation is closer to the left side 
#of the histogram, indicating smaller time values (plotted on the x-axis), while the distribution of the linked list implementation
#is closer to the right side of the histogram, which indicates larger time values. This is likely due to the fact that push and pop
#operations in an array simply utilize the append() and pop() methods of Python arrays, whereas push and pop operations in a linked
#list require the creation of a new node and moving the head and next pointers to their appropriate places. 
