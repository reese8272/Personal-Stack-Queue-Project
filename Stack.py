import numpy as np

class Stack:
    def __init__(self, _array_size = 1000):
        '''Constructs a Stack Object'''
        self._array_size = _array_size      # arrays are fixed size
        self._next_avail = 0
        self._lst = np.empty(self._array_size, dtype=object)  #constructor for array of None

    def push(self, element):
        '''Adds an element to the stack'''
        if self.is_full():
            return "Stack is full."
        self._lst[self._next_avail] = element
        self._next_avail += 1

    def pop(self):
        '''Retrieves the next element needed from the stack'''
        if self.is_empty():
            return None
        self._next_avail -= 1
        value = self._lst[self._next_avail]
        self._lst[self._next_avail] = None
        return value

    def is_empty(self):
        '''Returns the truth value of whether the stack is empty or not'''
        return self._next_avail == 0

    def is_full(self):
        '''Returns the truth value of whether the stack is full or not'''
        return self._next_avail == np.size(self._lst)

    def __repr__(self):       # called by print() or str() or repr()
        return 'Stack ADT'