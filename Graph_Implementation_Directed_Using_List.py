#Directed Graph implementation using adjacency list

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    #4,9: means 4=>[9]
    def add_edge(self,i,j):
        self.graph[i].append(j)

    def print_graph(self):
        for val in self.graph:
            for k in self.graph[val]:
                print(val,"->",k)


#248591

g=Graph()
g.add_edge(2,4)
g.add_edge(4,8)
g.add_edge(8,5)
g.add_edge(5,9)
g.add_edge(9,1)
g.add_edge(1,2)

g.print_graph()