def latticemaker(n):
    latticelist=[]
    for x in range(n):
        for y in range(n):
            latticelist.append([x,y])

    return latticelist
def moveset():
    return [[2,1],[2,-1],[-2,-1],[-2,1],[1,2],[1,-2],[-1,-2],[-1,2]]
def vectoradd(n,k):
    
    for i in range(len(n)):
      n[i]+=k[i] 
       
    return n

def horsegraph(n):
    #this isn't done
    lattice=latticemaker(n)
    movesets=moveset()
    for n in lattice:
        for k in movesets:
            Ll=vectoradd(n,k)
            if Ll in lattice:
                print(vectoradd(n,k))
                continue
            else:
                continue
    return 
print(latticemaker(5))