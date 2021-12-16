#Shortest Reach possible, Graph Algorithm by Ziithe Ewen Hiwa

import sys

class Graph:
    #initilise dictionary of the nodes and weight
    def __init__(self, n):
        self.size = n
        self.vertex = dict.fromkeys([n for n in range(n)])
        for node in self.vertex.keys():
            self.vertex[node] = {}
        
    def print_graph(self):
        print(self.vertex)

    def add_edge(self, x, y, w):
        #add the edges to graph
        if not y in self.vertex[x].keys() or self.vertex[x][y] > w:
            self.vertex[x][y] = w
            self.vertex[y][x] = w

    def shortestReach(self, graph, start):
        path = [-1] * graph.size
        path[start] = 0
        #list of all visited edges
        visited = []
        #initilise next edge from 0
        next_edge = {start:0}
        
        while bool(next_edge):
            #check for edge with least weight
            node = min(next_edge, key=next_edge.get)
            #delte already visited vertex
            del next_edge[node]
            
            #check to add node to path
            for child in graph.vertex[node].keys():
                if not child in visited:
                    temp_path = path[node] + graph.vertex[node][child]
                    if path[child] == -1 or path[child] > temp_path:
                        path[child] = temp_path
                        next_edge[child] = temp_path
                    
            visited.append(node)
        
        del path[start]
        return path
        

#get the number of test cases    
t = int(input().strip())
#initialise loop of test cases
for i in range(t):
    #get nodes and edges
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]
    #call graph function with number of nodes
    graph = Graph(n)
    for a in range(m):
        #get the edges with weights
        x,y,r = input().strip().split(' ')
        x,y,r = [int(x),int(y),int(r)]
        #add edges to graph
        graph.add_edge(x - 1, y - 1, r)
    #get starting node as s
    s = int(input().strip())
    #call shortestReach function
    result = graph.shortestReach(graph, s-1)
    print ("The Shortest Path Values: ", " ".join(map(str, result)))