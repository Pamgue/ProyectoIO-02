mine1 = [[1,3,3],
        [2,1,4],
        [0,6,4]]

mine2 = [[1,3,1,5],
        [2,2,4,1],
        [5,0,2,3],
        [0,6,1,2]]

mine3 = [[10,33,13,15],
         [22,21,4,1],
         [5,0,2,3],
         [0,6,14,2]]

def max_aux(aux):

    max = -10000
    index = -1
    for i in range(0,3):
        if(aux[i] > max):
  
            
            max = aux[i]
            index = i

    return index,max


def fill(row,col):
    memo = []
    route = []
    for i in range(row):
        memo_aux = []
        route_aux = []
        for j in range(col):
            memo_aux.append(-1000000)
            route_aux.append([0])
        memo.append(memo_aux)
        route.append(route_aux)

    return memo,route

def bottomUpGoldMine(mine,row,col):
    indexes = [-1,0,1]
    gold_dp,route = fill(row,col)

    for i in range(0,row):
        gold_dp[i][0] = mine[i][0]
    
    for j in range(1,col):
        for i in range(0,row):
            left = gold_dp[i][j-1]
            if(i == 0): 
                left_down = gold_dp[i+1][j-1]
                left_up = 0
            elif(i == row - 1):
                left_up = gold_dp[i-1][j-1]
                left_down = 0
            else:
                left_down = gold_dp[i+1][j-1]
                left_up = gold_dp[i-1][j-1]
            
            gold_dp[i][j] = mine[i][j] + max(left_down,left,left_up)


            aux = [left_up,left,left_down]

            aux_index,max_value = max_aux(aux)  

           
            route_aux = i+indexes[aux_index]

            route[i][j] = route[route_aux][j-1]+[route_aux]
            gold_dp[i][j] = mine[i][j] + max_value


    max_value = gold_dp[0][col-1]
    max_route = route[0][col-1]
    j=0
    for i in range(1,row):
        if(gold_dp[i][col-1] > max_value):
            max_value = gold_dp[i][col-1]
            max_route = route[i][col-1]
            j=i
    print('Output: ' + str(max_value))
    final_route = max_route[1:] + [j]
    #print(final_route)
    for i in range(0,col):
       print('('+str(final_route[i])+','+str(i)+')')
                


def topDownGoldMine(mine,N,M):


    dp,route = fill(N,M)

    for i in range(0,N):
        dp[i][M-1] = dp_max(mine,dp,i,M-1,N,M,route)
    
    max_value = dp[0][M-1]
    max_route = route[0][M-1]
    j=0
    for i in range(1,N):
        if(dp[i][M-1] > max_value):
            max_value = dp[i][M-1]
            max_route = route[i][M-1]
            j=i
    print('Output: ' + str(max_value))
    final_route = max_route[1:] + [j]

    for i in range(0,M):
       print('('+str(final_route[i])+','+str(i)+')')

def dp_max(mine,dp,i,j,N,M,route):
    indexes = [1,0,-1]
    
    if(i < 0 or i == N): #si no hay diagonales retorne 0
        return 0

    elif(j == 0):
        dp[i][j] = mine[i][j]

    elif(dp[i][j]!=-1000000):
        return dp[i][j]

    else:

        left_down = i+1
        left_up = i-1

        aux = [dp_max(mine, dp, left_down, j-1, N, M,route),dp_max(mine, dp, i, j-1, N, M,route),dp_max(mine, dp, left_up, j-1, N, M,route)]

        aux_index,max_value = max_aux(aux)
 
        route_aux = i+indexes[aux_index]

        route[i][j] = route[route_aux][j-1]+[route_aux]
        dp[i][j] = mine[i][j] + max_value

    return dp[i][j]

print('--------------mina 1----------')
print('------------Bottom Up---------')
bottomUpGoldMine(mine1,3,3)
print('-----------Top Down-----------')
topDownGoldMine(mine1, 3, 3)

print('--------------mina 2----------')
print('------------Bottom Up---------')
bottomUpGoldMine(mine2,4,4)
print('-----------Top Down-----------')
topDownGoldMine(mine2, 4, 4)

print('--------------mina 3----------')
print('------------Bottom Up---------')
bottomUpGoldMine(mine3,4,4)
print('-----------Top Down-----------')
topDownGoldMine(mine3, 4, 4)


        

   

