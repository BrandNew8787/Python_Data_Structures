from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x: np.object):
            self.next = None
            self.x = x

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def push(self, x: np.object):
        new_node = self.Node(x)
        new_node.next = self.head
        self.head = new_node
        if self.n == 0:
            self.tail = new_node
        self.n += 1
        return x

    def pop(self) -> np.object:
        if self.n == 0:
            raise Exception("List is empty.")
        x = self.head
        self.head = self.head.next
        self.n -= 1
        if self.n == 0:
            self.tail = None
        return x.x

    def size(self) -> int:
        return self.n

    def reverse(self):
        self.tail = self.head
        next_node = None
        previous_node = None
        for i in range(self.n):
            next_node = self.head.next
            self.head.next = previous_node
            previous_node = self.head
            self.head = next_node
        self.head = previous_node

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x

