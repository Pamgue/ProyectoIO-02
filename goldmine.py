

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


def fill(row,col):
    memo = []
    for i in range(row):
        memo_aux = []
        for j in range(col):
            memo_aux.append(0)
        memo.append(memo_aux)
    return memo

def bottomUpGoldMine(mine,row,col):
    gold_dp = fill(row,col)

    for i in range(0,row):
        gold_dp[i][0] = mine[i][0]
    
    for j in range(1,col):
        for i in range(0,row):
            left = gold_dp[i][j-1]
            if(i == 0): ## si es el borde superior de la mina no puede conseguir oro arriba a la izquierda
                left_down = gold_dp[i+1][j-1]
                left_up = 0
            elif(i == row - 1):
                left_up = gold_dp[i-1][j-1]
                left_down = 0
            else:
                left_down = gold_dp[i+1][j-1]
                left_up = gold_dp[i-1][j-1]
            
            gold_dp[i][j] = mine[i][j] + max(left_down,left,left_up)

    max_value = gold_dp[0][row-1]
    for i in range(1,row):
        if(gold_dp[i][col-1] > max_value):
            max_value = gold_dp[i][col-1]
    print(max_value)
            


##buscar otra manera de imprimir ruta
def print_route(gold_dp,row,col):
    route = [0]
    max = gold_dp[0][row-1]
    for i in range(1,row):
        if(gold_dp[i][col-1] > max):
            max = gold_dp[i][col-1]
            route = [i]
    i = route[0]
    for j in reversed(range(0,col)):
        if(i == 0):
            left_up = -10000
            left_down = gold_dp[i+1][j-1]
            left = gold_dp[i][j-1]

            i = aux_i(left_up,left,left_down,i)
        elif(i == row - 1):
            left_down = -10000
            left_up = gold_dp[i-1][j-1]
            left = gold_dp[i][j-1]

            i = aux_i(left_up,left,left_down,i)
        else:
            left_up = gold_dp[i-1][j-1]
            left_down = gold_dp[i+1][j-1]
            left = [i][j-1]

            i = aux_i(left_up,left,left_down,i)
        route.append(i)
    

    print(route)
    for i in reversed(range(0,row)):
        print(route[i])

    

def aux_i(left_up,left,left_down,i):
    if(left_up > left_down & left_up > left):
            route.append(i-1)
            i -= 1
    elif(left_down > left_up & left_down > left):
            route.append(i+1)
            i += 1
    return i
    
    

    

bottomUpGoldMine(mine1,3,3)
bottomUpGoldMine(mine2,4,4)
bottomUpGoldMine(mine3,4,4)
        

   

        

   

