"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue
import SLLQueue


class AdjacencyList(Graph):
    def __init__(self, n: int):
        self.n = n
        self.adj = np.zeros(self.n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def new_boolean_matrix(self, n):
        return np.zeros([n, n], np.bool_)

    def new_boolean_array(self, n):
        return np.zeros(n, np.bool_)

    def add_edge(self, i: int, j: int):
        self.adj[i].append(j)

    def remove_edge(self, i: int, j: int):
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return

    def has_edge(self, i: int, j: int) -> bool:
        for k in self.adj[i]:
            if k == j:
                return True
        return False

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, i) -> List:
        out = ArrayList.ArrayList()
        for j in range(self.n - 1):
            if self.has_edge(j, i):
                out.append(j)
        return out

    def bfs(self, r: int):
        seen = self.new_boolean_array(self.n)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            print(i, end=' ')
            ngh = self.out_edges(i)
            for k in range(ngh.size()):
                j = ngh.get(k)
                if seen[j] == False:
                    q.add(j)
                    seen[j] = True

    def dfs(self, r: int):
        seen = self.new_boolean_array(self.n)
        s = ArrayStack.ArrayStack()
        s.push(r)
        while s.size() > 0:
            i = s.pop()
            print(i, end=' ')
            seen[i] = True
            ngh = self.out_edges(i)
            for j in range(ngh.size()):
                if seen[ngh.get(j)] == False:
                    s.push(ngh.get(j))
                else:
                    continue
                    print(f"{i} and {j} are in a cycle")

    def bfs2(self, r, p):
        seen = self.new_boolean_array(self.n)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        l = []
        d = 0
        seen[r] = True
        while q.size() > 0 and d < p:
            i = q.remove()
            ngh = self.out_edges(i)
            for k in range(ngh.size()):
                j = ngh.get(k)
                if seen[j] == False:
                    q.add(j)
                    l.append(j)
                    seen[j] = True
            d += 1
        return l

    def dfs2(self, r1: int, r2: int):
        seen = self.new_boolean_array(self.n)
        s = ArrayStack.ArrayStack()
        d = np.zeros(self.n, object)
        s.push(r1)
        d[r1] = 0
        while s.size() > 0:
            i = s.pop()
            seen[i] = True
            ngh = self.out_edges(i)
            for j in range(ngh.size()):
                if seen[ngh.get(j)] == False:
                    s.push(ngh.get(j))
                    d[ngh.get(j)] = d[i] + 1
                    if ngh.get(j) == r2:
                        return d[ngh.get(j)]
        return -1

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

def main():
    g = AdjacencyList(6)
    print(g.remove_edge(3, 5))
    print(g.has_edge(3, 5))
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 1)
    g.add_edge(1, 3)
    print(g.has_edge(1, 2))
    print(g.has_edge(2, 1))
    print(g.in_edges(3))
    print(g.out_edges(1))
    g.bfs(1)
    print()
    g.dfs(1)
    print()


if __name__ == "__main__":
    main()