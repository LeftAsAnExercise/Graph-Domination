def latticemaker(n):
    latticelist=[]
    for x in range(n):
        for y in range(n):
            latticelist.append([x,y])

    return latticelist
def moveset(r,s):
    return [[r,s],[r,-s],[-r,-s],[-r,s],[s,r],[s,-r],[-s,-r],[-s,r]]
def vectoradd(n,k):
    placeholder=n
    for i in range(len(placeholder)):
      placeholder[i]+=k[i] 
       
    return placeholder



    
def rsLeaperGraph(n,r,s):
    lattice=latticemaker(n)
    banana=moveset(r,s)
    print(lattice)
    graph=dict()
    for x in range(n):
        for y in range(n):
            graph[lattice.index([x,y])]=[]
            for k in banana:
                if vectoradd([x,y],k) in lattice:
                    graph[lattice.index([x,y])].append(lattice.index(vectoradd([x,y],k)))
                    continue
                else:
                    continue
    print(graph)
    return
rsLeaperGraph(3,1,2)
            

