import numpy as np

class Queue:
    def __init__(self):
        '''Constructs the Queue Object'''
        self._array_size = 10
        self._lst = np.empty(self._array_size, dtype=object)
        self._next_pop = 0
        self._next_push = 0

# Ring Queue Method, in which we simply push and pop the queue wherever it falls without shifting anything
    def _rotate_(self,next_element):
        if next_element == np.size(self._lst)-1:
            next_element = 0
        else: next_element += 1
        return next_element
    
    def is_full(self):
        '''Returns the truth value of whether or not the the Queue is full'''
        return self._lst[self._next_push] is not None

    def is_empty(self):
        '''Returns the truth value of whether or not the Queue is empty'''
        return self._lst[self._next_pop] is None

    def push(self,element):
        if self.is_full():
            return "Queue is Full"
        self._lst[self._next_push] = element
        self._next_push = self._rotate_(self._next_push)
    
    def pop(self):
        '''Return the oldest element added to the queue that hasn't been popped. The Queue is First In, First Out'''
        if self.is_empty():
            return "Queue is Empty"
        value = self._lst[self._next_pop]
        self._lst[self._next_pop] = None
        self._next_pop = self._rotate_(self._next_pop)
        return value


        
# Shift method, in which we take the first element, and then shift the rest of the Queue one left
        
#    def push(self,element):
#        '''Adds an element to the queue, and will return "Queue is full" if nothing can be added to the queue'''
#        if self.is_full():
#            return "Queue is full."
#        return super().push(element)
        
#    def pop(self):
#        '''Return the oldest element added to the queue that hasn't been popped. The Queue is First In, First Out'''
#        if self.is_empty():
#            return None
#        value = self._lst[0]
#        self._next_avail -= 1
#        COUNTER = 0
#        for CHECKER in range(1,len(self._lst)):
#            if self._lst[CHECKER] == None:
#                break
#            self._lst[COUNTER] = self._lst[CHECKER]
#            COUNTER += 1
#        return value