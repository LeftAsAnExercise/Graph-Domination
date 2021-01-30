# First networkx library is imported  
# along with matplotlib 
import networkx as nx 
import matplotlib.pyplot as plt 
   
  
# Defining a Class 
class GraphVisualization: 
   
    def __init__(self): 
          
        # visual is a list which stores all  
        # the set of edges that constitutes a 
        # graph 
        self.visual = [] 
          
    # addEdge function inputs the vertices of an 
    # edge and appends it to the visual list 
    def addEdge(self, a, b): 
        temp = [a, b] 
        self.visual.append(temp) 
          
    # In visualize function G is an object of 
    # class Graph given by networkx G.add_edges_from(visual) 
    # creates a graph with a given list 
    # nx.draw_networkx(G) - plots the graph 
    # plt.show() - displays the graph 
    def visualize(self): 
        G = nx.Graph() 
        G.add_edges_from(self.visual) 
        nx.draw_networkx(G) 
        plt.show() 
  
# Driver code



def generateBishopsGraph(n):
    graph = dict()
    for i in range(n):
        for j in range(1,n+1):
            s = chr(i+97) + str(j)
            graph[s] = []
            for k in range(-n,n):
                index = j + k
                letter = i + k
                if not (letter < 0 or letter > n-1) and not (index <= 0 or index > n) and not (k == 0):
                    v = chr(letter+97) + str(index)
                    graph[s].append(v)
                index = j - k
                letter = i + k
                if not (letter < 0 or letter > n-1) and not (index <= 0 or index > n) and not (k == 0):
                    v = chr(letter+97) + str(index)
                    graph[s].append(v)
    return graph


if __name__ == "__main__":
    n = 20
    size = n
    graph = generateBishopsGraph(n)
    vertexes = graph.keys()
    G = GraphVisualization() 
    for i in vertexes:
        for j in graph[i]:
            G.addEdge(i,j)

    G.visualize() 


