# First networkx library is imported  
# # along with matplotlib 
# import networkx as nx 
# import matplotlib.pyplot as plt 
   
  
# # Defining a Class 
# class GraphVisualization: 
   
#     def __init__(self): 
          
#         # visual is a list which stores all  
#         # the set of edges that constitutes a 
#         # graph 
#         self.visual = [] 
          
#     # addEdge function inputs the vertices of an 
#     # edge and appends it to the visual list 
#     def addEdge(self, a, b): 
#         temp = [a, b] 
#         self.visual.append(temp) 
          
#     # In visualize function G is an object of 
#     # class Graph given by networkx G.add_edges_from(visual) 
#     # creates a graph with a given list 
#     # nx.draw_networkx(G) - plots the graph 
#     # plt.show() - displays the graph 
#     def visualize(self): 
#         G = nx.Graph() 
#         G.add_edges_from(self.visual) 
#         nx.draw_networkx(G) 
#         plt.show() 
  
# # Driver code



def generateRooksGraph(n):
    graph = dict()
    for i in range(n): # horizontal (letters / other ASCII characters)
        for j in range(1,n+1): #vertical (numbers)
            s = chr(i+97) + str(j)
            graph[s] = []

            moves_across = [chr(i+97) + str(k + 1) for k in range(n)]
            moves_vertical = [chr(k+97) + str(j) for k in range(n)]

            graph[s].append(moves_across + moves_vertical)
            
    return graph


if __name__ == "__main__":
    # n = 20
    # size = n
    graph = generateRooksGraph(8) # 1 - 8
    print(graph)
    # vertexes = graph.keys()
    # G = GraphVisualization() 
    # for i in vertexes:
    #     for j in graph[i]:
    #         G.addEdge(i,j)

    # G.visualize() 


