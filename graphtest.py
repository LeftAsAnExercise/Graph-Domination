
def generateRooksGraph(n):
    graph = dict()
    for i in range(n): # horizontal (letters / other ASCII characters)
        for j in range(1,n+1): #vertical (numbers)
            s = chr(i+97) + str(j)
            graph[s] = []

            moves_horizontal = [chr(i+97) + str(k + 1) for k in range(n)]
            moves_vertical = [chr(k+97) + str(j) for k in range(n)]

            graph[s].append(moves_horizontal + moves_vertical)
            
    return graph


if __name__ == "__main__":
    graph = generateRooksGraph(8) # 1 - 8
    print(graph)



