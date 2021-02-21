def getNodes(d):
    nodes = []
    for i in d.keys():
        if i not in nodes:
            nodes.append(i)
        for j in d[i]:
            if j not in nodes:
                nodes.append(j)

    return len(nodes)

def calculateObjectiveFunction(length, graphDictionary, solutionVector):
    
    d = dict()
    for i in range(len(solutionVector)):
        if solutionVector[i]:
            d[i] = graphDictionary[i]
    V = length ** 2
    n = getNodes(d)
    G = solutionVector.count(1)
    return n/V + 1/(V*G)
    

if __name__ == "__main__":
    print(calculateObjectiveFunction(3,{0: [5, 7], 1: [8, 6], 2: [3, 7], 3: [8, 2], 4: [], 5: [6, 0], 6: [5, 1], 7: [0, 2], 8: [3, 1]},[0,0,0,1,0,1,0,0,0]))


