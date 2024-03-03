import random 
import timeit

class PriorityQueue1:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        self.merge_sort(0, len(self.items)-1)
    
    def dequeue(self):
        if len(self.items) == 0:
            return
        return self.items.pop(0)
    
    def merge_sort(self,low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)

    def merge( self, low, mid, high):
        left = []
        right = []
        for i in range(low, mid + 1):
            left.append(self.items[i])
        for i in range(mid + 1, high + 1):
            right.append(self.items[i])

        

        left_i = 0
        right_i = 0
        array_i = low

        while True:
            if left_i >= len(left) or right_i >= len(right):
                break
            if left[left_i] > right[right_i]:
                self.items[array_i] = right[right_i]
                right_i += 1
            else:
                self.items[array_i] = left[left_i]
                left_i += 1
            array_i += 1

        while left_i < len(left):
            self.items[array_i] = left[left_i]
            left_i+=1
            array_i +=1

        while right_i < len(right):
            self.items[array_i] = right[right_i]
            array_i+=1
            right_i +=1



class PriorityQueue2:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        i = 0
        while i < len(self.items) and item >= self.items[i]:
            i+=1
        self.items.insert(i, item)

        
    
    def dequeue(self):
        if len(self.items) == 0:
            return
        return self.items.pop(0)
    

def random_task_generator():
    e_count = 0
    d_count = 0
    tasks = []

    while e_count != 700:
        newtask = []
        newtask.append('enqueue')
        newtask.append(random.randint(0,100))
        tasks.append(newtask)
        e_count+=1

    while d_count != 300:
        newtask = []
        newtask.append('dequeue')
        tasks.append(newtask)
        d_count+=1

    random.shuffle(tasks)
    return tasks

def first_performance(tasks, priorityq):
    for task in tasks:
        if task[0] == 'enqueue':
            priorityq.enqueue(task[1])
        else:
            priorityq.dequeue()

def second_performance(tasks, priorityq):
    for task in tasks:
        if task[0] == 'enqueue':
            priorityq.enqueue(task[1])
        else:
            priorityq.dequeue()

def main():
    priorityq1_times = []
    priorityq2_times = []
    i = 0
    while i< 100:
        tasks = random_task_generator()
        priorityqueue1 = PriorityQueue1()
        priorityqueue2 = PriorityQueue2()
        priorityq1_times.append(timeit.timeit(lambda:first_performance(tasks, priorityqueue1), number = 1))
        priorityq2_times.append(timeit.timeit(lambda:second_performance(tasks, priorityqueue2), number = 1))
        i+=1
    result1 = sum(priorityq1_times)/100
    result2 = sum(priorityq2_times)/100

    print('The sorting implementation of priority queue took: ', result1, 's')
    print('The insertion implementation of priority queue took: ', result2, 's')
    


#5. 
    # The insertion implementation is faster, with an average execution time of 0.010898740992415697s.
    # This is way less than the time it took for the mergesort implementation (0.970906455994118s).
    # Since the enqueue with the mergesort has a time complexity of O(nlogn) due to the sorting algorithm,
    # and the enqueue with the insertion has time complexity O(n) (finding the right index for insertion takes n iterations
    # in the worst case), we can compare their efficiencies. O(n) is better than O(nlogn) in terms of
    # performance, and thus it is expected that the insertion implementation is faster.



if __name__ == '__main__':
    main()