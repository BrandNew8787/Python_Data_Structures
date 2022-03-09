import numpy as np
from Interfaces import Stack


class ArrayStack(Stack):
    '''
        ArrayStack: Implementation of the Stack interface based on Arrays.
        All the @abstractemthods should be implemented.
        An instance of ArrayStack has access to all the methods in ArrayStack and
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack).
        For exmaple,
        s = ArrayStack()
        print(s)
        print(len(s))
    '''

    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) -> np.array:
        return np.zeros(n, np.object)

    def resize(self):
        y = self.new_array(max(1, 2 * self.n))
        y[0:self.n] = self.a[0:self.n]
        self.a = y

    def get(self, i: int) -> np.object:
        return self.a[i]

    def set(self, i: int, x: np.object) -> object:
        if self.n == 0 or i > self.n or i < 0:
            raise Exception("Out of bounds or nothing in the array.")
        else:
            y = self.a[i]
            self.a[i] = x
            return y

    def add(self, i: int, x: np.object):
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        if self.n >= len(self.a) or self.n < 0:
            self.resize()
        self.a[i + 1: self.n + 1] = self.a[i:self.n]
        self.a[i] = x
        self.n += 1

    def element(self) -> int:
        return self.n

    def remove(self, i: int) -> np.object:
        '''
            remove element i and shift all j > i one
            position to the left
        '''
        if self.n == 0 or i > self.n or i < 0:
            raise Exception("The array is empty or i is Out of Bounds.")
        else:
            x = self.a[i]
            self.a[i: self.n - 1] = self.a[i + 1: self.n]
            self.n -= 1
            if len(self.a) > self.n * 3 or self.n < len(self.a):
                self.resize()
            return x

    def push(self, x: np.object):
        self.add(self.n, x)

    def pop(self) -> np.object:
        return self.remove(self.n - 1)

    def size(self):
        '''
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        '''
        return self.n

    def __str__(self) -> str:
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayStack
            Return: String with the content of the stack
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        '''
            Initialize the iterator. It is to be use in for loop
        '''
        self.iterator = 0
        return self

    def __next__(self):
        '''
            Move to the next item. It is to be use in for loop
        '''
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator += 1
        else:
            raise StopIteration()
        return x