#Directed Graph implementation using adjacency matrix

class Graph:
    def __init__(self, no_of_nodes):
        #5->[1,2,3,4,5]
        self.no_of_nodes=no_of_nodes+1
        self.graph=[[0 for i in range(no_of_nodes+1)] for j in range(no_of_nodes+1)]

    def add_edge(self,a1,a2):
        if ((a1>=0 and a1 <=self.no_of_nodes) and (a2>=0 and a2 <=self.no_of_nodes)):
            self.graph[a1][a2]=1

    def print_graph(self):
        for i in range(self.no_of_nodes):
            for j in range(len(self.graph[i])):
                if self.graph[i][j]:
                    print(i,"->",j)

g=Graph(6)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(4,5)
g.add_edge(5,6)
g.print_graph()