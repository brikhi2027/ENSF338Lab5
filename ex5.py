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
        return

        
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

class ListQueue:
    def __init__(self, capacity):
        self._head = None
        self._tail = None
        self._size = 0
        self._capacity = capacity
    def enqueue(self, value):
        new_node = ListNode(value)
        if self._head is None:
            self._head = new_node
            self._tail = self._head
            self._head._next = self._head # set the next pointer of the only node to point to itself
            print('enqueue', value)
        elif self._size < self._capacity:
            self._tail._next = new_node
            print('enqueue', value)
            self._tail = new_node
            self._tail._next = self._head
        else:
            print('enqueue None')
        self._size += 1

    def dequeue(self):
        if self._head is None:
            print('dequeue None')
            return
        temp = self._head._value

        if (self._head == self._tail) and (self._head._next == None):
            self._head = None
            self._tail = None
            print('dequeue', temp)
        else:
            self._head = self._head._next
            self._tail._next = self._head
            print('dequeue', temp)
        return temp
    
    def peek(self):
        if self._head is None:
            print('peek None')
            return
        else:
            first_node = self._head._value
        print('peek', first_node)
        return
                    
      
# 3. Generate a list of 40 operations, together with expected output, that can
# be used to test correctness of implementation. [0.2 pts]

def test_implementation(queue):
    my_queue.dequeue() # test 1: dequeueing from empty queue
    print('Expected: dequeue None\n')

    my_queue.peek() # test 2: peeking into empty queue
    print('Expected: peek None\n')

    my_queue.enqueue(1) # test 3: enqueueing into empty queue
    print('Expected: enqueue 1\n')
    
    # tests 4 - 20: some regular enqueue operations
    for i in range(2, 19):
        my_queue.enqueue(i) # a regular enqueue operation
        expected_output = 'enqueue ' + str(i)
        print('Expected:',expected_output,'\n')

    my_queue.enqueue(2) # test 21: enqueueing into full queue
    print('Expected Output: enqueue None\n')
    
    # tests 22 - 39: some regular dequeuing and peek operations
    k = 1
    for i in range(0, 9):
        my_queue.peek()
        expected_output2 = 'peek ' + str(k)
        print('Expected:',expected_output2,'\n')

        my_queue.dequeue() # a regular dequeue operation
        expected_output = 'dequeue ' + str(k)
        print('Expected:',expected_output, '\n')
        k += 1
    
    my_queue.dequeue() # test 40: a regular dequeue operation
    expected_output = 'dequeue 10'
    print('Expected:',expected_output, '\n')

my_queue = ListQueue(18)
test_implementation(my_queue)

