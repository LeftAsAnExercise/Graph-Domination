def generateBishopsGraph(n):
    graph = dict()
    for i in range(n):
        for j in range(1,n+1):
            currentSquare = chr(i+97) + str(j) # a1
            graph[currentSquare] = []
            for k in range(-n,n):
                index = j + k
                letter = i + k
                if not (letter < 0 or letter > n-1) and not (index <= 0 or index > n) and not (k == 0):
                    validMove = chr(letter+97) + str(index)
                    graph[currentSquare].append(validMove)
                index = j - k
                letter = i + k
                if not (letter < 0 or letter > n-1) and not (index <= 0 or index > n) and not (k == 0):
                    validMove = chr(letter+97) + str(index)
                    graph[currentSquare].append(validMove)
    return graph
#Maybe add currentsquare into list
def generateKingsGraph(n):
    graph = dict()
    for i in range(n):
        for j in range(1,n+1):
            currentSquare = chr(i+97) + str(j)
            graph[currentSquare] = []
            for k in range(-1,2):
                for l in range(-1,2):
                    letter = i + k
                    index = j + l
                    if not (letter < 0 or letter > n-1) and not (index <= 0 or index > n) and not (k==0 and l==0):
                        validMove = chr(letter+97) + str(index)
                        graph[currentSquare].append(validMove)
    return graph

print(generateKingsGraph(3))