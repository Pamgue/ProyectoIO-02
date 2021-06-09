def generateMemo(n,m):
    mn = []
    for _ in range(n):
        fila = [0 for i in range(m)]
        mn.append(fila)
    return mn

#val = [0, 50, 26, 26]
#wt = [0, 7, 4, 4]
#W = 8


wt = [0,5,15,10,10,8]
val = [0,20,50,60,62,40]



memo = generateMemo(6,31)  #items+1, tamano mochila +1

#Top Down
def topDownKnapsack(item, capacity, memo):
    if(capacity < 0):
        return -(1<<60)
    elif capacity == 0 or item == 0:
        return 0
    elif memo[item][capacity]:
        return memo[item][capacity]
    else:
        memo[item][capacity] = max(val[item] + topDownKnapsack(item-1, capacity - wt[item],memo), topDownKnapsack(item-1,capacity,memo))
    return memo[item][capacity]



def SET(n,i):
    return n | (1<<i)

def TEST(n,i):
    return n & (1<<i)   

def choosenItems(matDP):
    row = len(matDP)-1
    col = len(matDP[0])-1
    msk = 0
    while row:
        if matDP[row][col] != matDP[row-1][col]:
            msk = SET(msk, row)
            col-=wt[row]
        row-=1
    return msk

def printChoosen(msk):
    for i in range(len(wt)):
        if(TEST(msk,i)):
            print(i)
            
###############################################################################


    
topDownKnapsack(5, 30, memo)
for i in memo:
    print(i)

printChoosen((choosenItems(memo)))



