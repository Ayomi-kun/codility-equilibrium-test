def addup(A,n):
    z = len(A)
    #z is parmanently the lenght of the array A
    x = n+1
    #x is the index right after the equilibrium index
    if(z-1 == x):
        q = A[x]
        return q
    else:
        q = 0
        while(x<=z-1):
            q = q + A[x]
            x = x + 1
        return q
def adddown(A,n):
    z = len(A)
    x = n-1
    if(x == 0):
        q = A[x]
        return q
    else:
        q = 0
        while(x>=0):
            q = q + A[x]
            x = x -1
        return q
#####main code
A = []
A.append(-1)
A.append(3)
A.append(-4)
A.append(5)
A.append(1)
A.append(-6)
A.append(2)
A.append(1)

z = len(A)
print A

check = False
for pivot in range(0,z):
    if(pivot == 0):
        if(addup(A,pivot) == 0):
            print "index ",pivot," is an equilibrium index."
            check = True
    elif(pivot>0 and pivot<z):
        if(addup(A,pivot) == adddown(A,pivot)):
            print "index ",pivot," is an equilibrium index."
            check = True
    else:
        continue
    
if(check == False):
    print"Index pivot for the equilibrium is -1"
