import random
import datetime
import sys
from copy import deepcopy
import time
import numpy as np
import itertools


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

I = 0
fileName = ""

def generateMineWithFile(listInputs):
    mine = []
    for i in listInputs:
        aux = []
        for j in i:
            aux.append(num(j))
        mine.append(aux)
    return mine

def generateRandomMine(N,M,min_value,max_value):
    mine = []    
    for i in range(N):
        aux = []
        for j in range(M):
            aux.append( random.randint(min_value, max_value))
        mine.append(aux)
    return mine


def readFile():
    lines = open(fileName, 'r').readlines()
    lines = list(map(removeEndLine, lines))
    listOfLists = []
    for line in lines:
        splittedLine = line.split(",")
        listOfLists.append(splittedLine)
    return listOfLists

def removeEndLine(line):
    if(line.endswith("\n")):
        return line.replace("\n", "")
    return line
def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def checkTime(mine,times,function):
    N = len(mine)
    M = len(mine[0])
    total_time = 0
    for i in range(1,times+1):
  
        start_time = datetime.datetime.now()
        if(function==2):
            dp,route = topDownGoldMine(mine, N, M)
        else:
            max,route = bruteForce(mine, N, M)
        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000

        #print('Iteration ' + str(i) + ' time: ' + str(execution_time))
        total_time += execution_time

    if(function==2):
        printTopDown(dp, route, N, M)
    else:
        printBruteForce(max,route,M)
        
    print('--------------------------------------------------')
    print('Average Execution Time: ' + str(total_time/times))

def main(args):
    global I
    if(args[1] == '1'): #bruteForce
        mine = processArg(args)
        if(type(mine)==str):
            return mine
        checkTime(mine, I, 1)
    elif(args[1] == '2'): #topDown
        mine = processArg(args)
        if(type(mine)==str):
            return mine
        #print(mine)
        checkTime(mine, I, 2)    
    else:
         return "Metodo no implementado"
        


def processArg(data):
    global fileName, I #N iteraciones
    if(len(data)==5): # con archivo
        fileName = data[3] #nombre de archivo
        I = num(data[4]) #iteraciones
        if(I <= 0):
            return "Valor de iteraciones incorrecto"
        else:
            listInputs = readFile()
            return generateMineWithFile(listInputs)
    elif(len(data) == 8):
        N = num(data[3])
        M = num(data[4])
        min_value = num(data[5])
        max_value = num(data[6])
        I = num(data[7])
        if(N <= 0 or M <= 0 or min_value < 0 or max_value <= 0 or max_value < min_value or I <= 0):
            return 'Parametros incorrectos'
        else:
            return generateRandomMine(N, M, min_value, max_value)


def max_aux(aux,N):

    max = -10000
    index = -1
    for i in range(0,N):
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

            aux_index,max_value = max_aux(aux,3)  

           
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



def bruteForceAux(mine,i,j,N,M,route):

    indexes = [1,0,-1]
    
    if(i < 0 or i == N): #si no hay diagonales retorne 0
        return 0

    elif(j==0):
        return mine[i][j]
    else:

        left_down = i+1
        left_up = i-1

        aux = [bruteForceAux(mine, left_down, j-1, N, M,route),bruteForceAux(mine,i, j-1, N, M,route),bruteForceAux(mine, left_up, j-1, N, M,route)]

        aux_index,max_value = max_aux(aux,3)
 
        route_aux = i+indexes[aux_index]

        route[i][j] = route[route_aux][j-1]+[route_aux]

        return mine[i][j] + max_value

def bruteForce(mine,N,M):
    solution = []
    x,route = fill(N, M)
    for i in range(N):
        solution.append(bruteForceAux(mine, i, M-1, N, M,route))

    #print(solution)
    max_index, max_value = max_aux(solution,N)
   

    final_route = route[max_index][M-1]
    final_route  = final_route[1:] + [max_index]

    return max_value,final_route
    #print(final_route)

def printBruteForce(max_value,final_route,M):
    print('Output: ' + str(max_value))
    for i in range(0,M):
       print('('+str(final_route[i])+','+str(i)+')')


def topDownGoldMine(mine,N,M):

    dp,route = fill(N,M)

    for i in range(0,N):
        dp[i][M-1] = dp_max(mine,dp,i,M-1,N,M,route)

    return dp,route

def printTopDown(dp,route,N,M):
    max_value = dp[0][M-1]
    max_route = route[0][M-1]
    j=0
    aux = [max_value]
    for i in range(1,N):
        aux.append(dp[i][M-1])
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

        aux_index,max_value = max_aux(aux,3)
 
        route_aux = i+indexes[aux_index]

        route[i][j] = route[route_aux][j-1]+[route_aux]
        dp[i][j] = mine[i][j] + max_value

    return dp[i][j]

'''
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

print(bruteForce(mine1,0,2, 3, 3))

        
'''

solution = main(sys.argv)
if(type(solution)==str):
    print(solution)

   


