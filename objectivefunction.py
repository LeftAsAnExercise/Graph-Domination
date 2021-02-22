from random import choice, uniform
from numpy import array, where
length = 3
#graphDictionary = {0: [5, 7], 1: [8, 6], 2: [3, 7], 3: [8, 2], 4: [], 5: [6, 0], 6: [5, 1], 7: [0, 2], 8: [3, 1]}
#
graphDictionary = {0 : [3,6,1,2], 1: [0,2,4,7], 2: [0,1,5,8], 3: [0,6,4,5], 4: [3,5,1,7], 5: [8,2,3,4], 6: [3,0,7,8], 7: [6,8,4,1], 8:[5,2,6,7]}
def getNodes(d):
    nodes = []
    for i in d.keys():
        if i not in nodes:
            nodes.append(i)
        for j in d[i]:
            if j not in nodes:
                nodes.append(j)

    return len(nodes)

def stochastic_local_search(solutionVector):
    print(calculateObjectiveFunction(solutionVector))
    while True:
        objective_function = calculateObjectiveFunction(solutionVector)
        if(objective_function >= 1):
            solutionVector[inverse_probability(solutionVector)] = 0
        else:
            solutionVector[proportional_probability(solutionVector)] = 1
        if calculateObjectiveFunction(solutionVector) < objective_function:
            i1 = int(choice(array(where(array(solutionVector) == 0)).T))
            i2 = int(choice(array(where(array(solutionVector) == 1)).T))
            solutionVector[i1], solutionVector[i2] = solutionVector[i2], solutionVector[i1]
        if(calculateObjectiveFunction(solutionVector) <= objective_function):
            break
    return solutionVector       


def calculateObjectiveFunction(solutionVector):
    d = dict()
    for i in range(len(solutionVector)):
        if solutionVector[i]:
            d[i] = graphDictionary[i]
    V = length ** 2
    n = getNodes(d)
    G = solutionVector.count(1)
    return n/V + 1/(V*G)
    
def proportional_probability(solutionVector):
    l = []
    for index, value in enumerate(solutionVector):
        if not value:
            l.extend([index] * len(graphDictionary[index]))
    return choice(l)

def inverse_probability(solutionVector):
    d = {}
    s = 0
    for index, value in enumerate(solutionVector):
        if value:
            s += 1/len(graphDictionary[index])
            d[s] = index
    p = uniform(0,s)
    for i in d.keys():
        if p <= i:
            return d[i]
            


if __name__ == "__main__":
    print(stochastic_local_search([1,0,0,0,0,0,0,0,0]))


