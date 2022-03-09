"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyMatrix(Graph):
    def __init__(self, n: int):
        self.n = n
        self.adj = self.new_boolean_matrix(self.n)

    def new_boolean_matrix(self, n):
        return np.zeros([n, n], np.bool_)

    def new_boolean_array(self, n):
        return np.zeros(n, np.bool_)

    def add_edge(self, i: int, j: int):
        self.adj[i][j] = True

    def remove_edge(self, i: int, j: int):
        self.adj[i][j] = False

    def has_edge(self, i: int, j: int) -> bool:
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        l = ArrayList.ArrayList()
        for j in range(self.n - 1):
            if self.has_edge(i, j):
                l.append(j)
        return l

    def in_edges(self, j) -> List:
        l = ArrayList.ArrayList()
        for i in range(self.n - 1):
            if self.has_edge(i, j):
                l.append(i)
        return l

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


def __str__(self):
    s = ""
    for i in range(0, self.n):
        s += "%i,%r\n" % (i, self.adj[i].__str__())
    return s


def main():
    g = AdjacencyMatrix(6)
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


if __name__ == "__main__":
    main()
