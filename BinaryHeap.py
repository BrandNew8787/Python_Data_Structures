import numpy as np
from Interfaces import Queue



def left(i : int):
    return 2 * i + 1

def right(i: int):
    return 2 * (i + 1)

def parent(i : int):
    return (i)//2

class BinaryHeap(Queue):
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)

    def resize(self):
        x = self.new_array(max(1, self.n*2))
        for i in range(0, self.n):
            x[i] = self.a[i]
        self.a = x

    def add(self, x : object):
        if len(self.a) == self.n:
            self.resize()
        self.a[self.n] = x
        self.n += 1
        self.bubble_up(self.n-1)

    def bubble_up(self, i):
        if i < 0 or i >= self.n :
            raise Exception("i is out of bounds.")
        p = parent(i)
        while i > 0 and self.a[i] < self.a[p]:
            self.a[i], self.a[p] = self.a[p], self.a[i]
            i = p
            p = parent(i)

    def remove(self):
        if self.n == 0:
            raise Exception("The array is empty.")
        x = self.a[0]
        self.a[0] = self.a[self.n-1]
        self.n -= 1
        self.trickle_down(0)
        if 3 * self.n < len(self.a):
            self.resize()
        return x

    def trickle_down(self, i):
        while i >= 0:
            j = -1
            r = right(i)
            if r < self.n and self.a[r] < self.a[i]:
                l = left(i)
                if self.a[l] < self.a[r]:
                    j = l
                else:
                    j = r
            else:
                l = left(i)
                if l < self. n and self.a[l] < self.a[i]:
                    j = l
            if j >= 0:
                self.a[j], self.a[i] = self.a[i], self.a[j]
            i = j

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i % len(self.a)]
            if i < self.n-1:
                s += ","
        return s + "]"



