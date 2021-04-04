from random import choice, uniform
from numpy import array, where
import random
import numpy
import math


graphDictionary = {0: [5, 7], 1: [8, 6], 2: [3, 7], 3: [8, 2], 4: [], 5: [6, 0], 6: [5, 1], 7: [0, 2], 8: [3, 1]}
print("banana")

def calculateObjectiveFunction(length, graphDictionary, solutionVector):
    d = dict()
    for i in range(len(solutionVector)):
        if solutionVector[i]:
            d[i] = graphDictionary[i]
    V = length ** 2
    n = getNodes(d)
    G = solutionVector.count(1)
    return n/V + 1/(V*G)


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


def proportional_probability(solutionVector):
    l = []
    for index, value in enumerate(solutionVector):
        if not value:

            temp1 = [index] * len(graphDictionary[index])
            
            l.extend(temp1)
            
    return choice(l)


def inverse_probability(solutionVector):
    d = {}
    s = 0
    for index, value in enumerate(solutionVector):
        if value:
            s += 1/len(graphDictionary[index])
            d[s] = index
    p = uniform(0, s)
    for i in d.keys():
        if p <= i:
            return d[i]


def NodeReduction(solutionVector):
    solutionVector[inverse_probability(solutionVector)] = 0
    return


def NodeAdd(solutionVector):
    solutionVector[proportional_probability(solutionVector)] = 1
    return


def NodeSwapper(solutionVector):
    i1 = int(choice(array(where(array(solutionVector) == 0)).T))
    i2 = int(choice(array(where(array(solutionVector) == 1)).T))
    solutionVector[i1], solutionVector[i2] = solutionVector[i2], solutionVector[i1]
    return


def getNodes(d):
    nodes = []
    for i in d.keys():
        if i not in nodes:
            nodes.append(i)
        for j in d[i]:
            if j not in nodes:
                nodes.append(j)

    return len(nodes)


def MainLoop(initTemp, finalTemp, CoolingRatio, EpochLength, initSolutionVector):
    XBest = initSolutionVector
    y = initSolutionVector
    Xk = initSolutionVector

    currentTemp = initTemp
    while currentTemp > finalTemp:
        for M in range(1, EpochLength+1):
            Temp1 = Xk
            y = Temp1
            if calculateObjectiveFunction( 3, graphDictionary, y) >= 1:
                NodeReduction(y)

                deltaFunction = calculateObjectiveFunction( 3, graphDictionary, y) - calculateObjectiveFunction( 3, graphDictionary, Xk)
                if deltaFunction > 0:
                    Temp1 = y
                    XBest = y
                    Xk = Temp1
                else:
                    probabilityAcceptance = 1 / (1 + math.exp(deltaFunction/currentTemp))
                    if random.random() < probabilityAcceptance:
                        Xk=y

                    else:
                        Xk=Xk
            else:
                NodeAdd(y)
                if calculateObjectiveFunction( 3, graphDictionary, y) > calculateObjectiveFunction( 3, graphDictionary, Xk):
                    Temp1=y
                    XBest=y
                    Xk=Temp1
            if calculateObjectiveFunction( 3, graphDictionary, y) < calculateObjectiveFunction( 3, graphDictionary, Xk):
                Temp1=Xk
                z=Temp1
                NodeSwapper(z)
                deltaFunction=calculateObjectiveFunction( 3, graphDictionary, z) - calculateObjectiveFunction( 3, graphDictionary, Xk)
                if deltaFunction > 0:
                    Temp1=z
                    XBest=z
                    Xk=Temp1
                else:
                    probabilityAcceptance=1 / (1 + math.exp(deltaFunction/currentTemp))
                    if random.random() < probabilityAcceptance:
                        Xk=z
                    else:
                        Xk=Xk

        if currentTemp > finalTemp:
            currentTemp *= CoolingRatio
            
            
        else:
            break
    return XBest
print(MainLoop(1500,150,0.95,10,[0,0,0,0,0,0,0,0,1]))
