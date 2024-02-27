#1. 
class Stack:
    def __init__(self):
        self._stack = []
        #self.max_size = 7500
        #self.tail = -1
    def push(self, element):
        self._stack.append(element)
        #self.tail += 1
        #if self.tail >= self.max_size:
            #print("Cannot add to a full stack.")
        #self.stack[self.tail] = element
    def pop(self):
        if self._stack == None:
            print("Cannot remove from an empty stack.")
            return None
        else:
            return self._stack.pop()
        #temp = self.stack[self.tail]
        #self.tail -= 1
        #return temp
    def peek(self):
        if self._stack == None:
            print("Stack is empty")
            return None
        return self._stack[-1]

arr = Stack()
arr.push(1)
arr.push(2)
arr.push(3)
arr.push(4)
arr.pop()
arr.pop()
a = arr.peek()
print(a)


