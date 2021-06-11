import random as rand
import sys
from copy import deepcopy
import time
import numpy as np
import itertools
import datetime
import matplotlib.pyplot as plt

fileName = ""
method = 0
N = 0
max_weight =0
val= []
wt =[]
times = []
def main(arg):
    global N, max_weight, times
    if(arg[1]== '1'):
        
        print("Fuerza bruta")
        matrix, origin = processArg(arg)
        for j in range(0, num(N)): # se toma el tiempo
            if origin == 2:
                print("Resultado:")
                start_time = datetime.datetime.now()
                itemsSlected,weigth,optimalValue =knapsack_brute_force(matrix,max_weight)
                print("Beneficio máximo: " + str(optimalValue))
                print("Incluidos: "+str(itemsSlected)[1:len(str(itemsSlected))-1])
                print("Resultado:")
                end_time = datetime.datetime.now()
                time_diff = (end_time - start_time)
                execution_time = time_diff.total_seconds() * 1000
                times.append(execution_time)
                print("Tiempo de ejecución: "+str(execution_time))
            else:
                print("Resultado:")
                max_weight=matrix[0][0]
                numMatrix = setUpKnapSack(matrix)
                start_time = datetime.datetime.now()
                itemsSlected,weigth,optimalValue =knapsack_brute_force(numMatrix,max_weight)
                print("Beneficio máximo: " + str(optimalValue))
                print("Incluidos: "+str(itemsSlected)[1:len(str(itemsSlected))-1])
                end_time = datetime.datetime.now()
                time_diff = (end_time - start_time)
                execution_time = time_diff.total_seconds() * 1000
                times.append(execution_time)

                print("Tiempo de ejecución: "+str(execution_time))
        suma = 0
        for i in times:
            suma = suma + i
        suma =  suma/len(times)
        print("Tiempor promedio de ejecución: "+str(suma))
        plt.plot(times)
        plt.ylabel('Tiempo de ejecución')
        plt.xlabel('Iteración')
        plt.show()
        
    elif(arg[1] == '2'):
        print("Bottom up")
        matrix, origin = processArg(arg)
        for j in range(0, num(N)): # se toma el tiempo
            if origin == 2:
                start_time = datetime.datetime.now()
                V = dynamicKnapSack(max_weight, matrix, len(matrix))
                print("Beneficio máximo: "+ str(V[len(matrix)][max_weight]))
                
                itemSelected,wtf=  findElements(V, max_weight,len(matrix), matrix)
                print("Incluidos: "+str(itemSelected)[1:len(str(itemSelected))-1])
                end_time = datetime.datetime.now()
                time_diff = (end_time - start_time)
                execution_time = time_diff.total_seconds() * 1000
                times.append(execution_time)
                print("Tiempo de ejecución: "+str(execution_time))
            

            else:
                numMatrix = setUpKnapSack(matrix)
                max_weight=matrix[0][0]
                print(setFormat(numMatrix))
                start_time = datetime.datetime.now()
                V = dynamicKnapSack(max_weight, numMatrix, len(numMatrix))
                print("Beneficio máximo: "+ str(V[len(numMatrix)][max_weight]))
                
                itemSelected,wtf=  findElements(V, max_weight,len(numMatrix), numMatrix)
                print("Incluidos: "+str(itemSelected)[1:len(str(itemSelected))-1])
                end_time = datetime.datetime.now()
                time_diff = (end_time - start_time)
                execution_time = time_diff.total_seconds() * 1000
                times.append(execution_time)
                print("Tiempo de ejecución: "+str(execution_time))
        suma = 0
        for i in times:
            suma = suma + i
        suma =  suma/len(times)
        print("Tiempor promedio de ejecución: "+str(suma))
        plt.plot(times)
        plt.ylabel('Tiempo de ejecución')
        plt.xlabel('Iteración')
        plt.show()
    elif (arg[1]== '3'):
        
        global val, wt
        print("top-down") 
        matrix, origin = processArg(arg)
        for j in range(0, num(N)): # se toma el tiempo
            if origin == 2:
                val, wt = setFormat(matrix)
                memo = generateMemo(len(val),max_weight+1)
                start_time = datetime.datetime.now()
                print("Beneficio máximo:" + str(topDownKnapsack((len(val)-1), max_weight, memo))) 
                printChoosen((choosenItems(memo)))
                end_time = datetime.datetime.now()
                time_diff = (end_time - start_time)
                execution_time = time_diff.total_seconds() * 1000
                times.append(execution_time)
                print("Tiempo de ejecución: "+str(execution_time))

            else:
                numMatrix = setUpKnapSack(matrix)
                max_weight = matrix[0][0]
                
                wt,val  = setFormat(numMatrix)
            
                memo = generateMemo(len(val),max_weight+1)
                start_time = datetime.datetime.now()
                print("Beneficio máximo:" + str(topDownKnapsack((len(val)-1), max_weight, memo))) 
                printChoosen((choosenItems(memo)))
                end_time = datetime.datetime.now()
                time_diff = (end_time - start_time)
                execution_time = time_diff.total_seconds() * 1000
                times.append(execution_time)
                print("Tiempo de ejecución: "+str(execution_time))
        suma = 0
        for i in times:
            suma = suma + i
        suma =  suma/len(times)
        print("Tiempor promedio de ejecución: "+str(suma))
        plt.plot(times)
        plt.ylabel('Tiempo de ejecución')
        plt.xlabel('Iteración')
        plt.show()
    else:
        print("Metodo no implementado")

def processArg(datos):
    global fileName, N
    if(len(datos) == 5):
        if(datos[2]=="-a"):
            fileName = datos[3]
            listOfData =readFile()
            N = num(datos[4])
            return formatMatrix(listOfData), 1
        else: 

            print("Existe un problema con los parametros del sistema")

    elif(len(datos) == 8 ):
        global max_weight
        if(datos[2]=="-p"):
            print("Procesando parametros")
            max_weight=  num(datos[3])
            elements = num(datos[4])
            weigth = datos[5].split('-')
            value = datos[6].split('-')
            value[0] = num(value[0])
            value[1] = num(value[1]) 
            weigth[0] = num(weigth[0])
            weigth[1] = num(weigth[1])
            N = num(datos[7])
            return build_items(elements, weigth, value),2


        else:
            print("Existe un problema con los parametros del sistema")    

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

def formatMatrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            matrix[row][column] = num(matrix[row][column])
            
    return matrix

def setUpKnapSack(matrix):
    global max_weight
    currentMatrix = matrix[1:]
    newMatrix=[]
    n = len(currentMatrix)
    currentId = 1
    for i  in currentMatrix:
        element = [currentId] + i
        currentId +=1
        newMatrix = newMatrix + [element]
    return newMatrix    
    


def build_items(n, w, v):
    res= []
    rand.seed(time.time())
    for i in range(n):
        res.append((i, rand.randint(w[0], w[1]), rand.randint(v[0], v[1])))

    print(max_weight)
    print(res)
    return res

def powerset(items):
    res = [[]]
    for item in items:
        newset = [r+[item] for r in res]
        res.extend(newset)
    
    return res


def knapsack_brute_force(items, max_weight):
    knapsack = []
    best_weight = 0
    best_value = 0
    ids =[]
    for item_set  in powerset(items):
        set_weight = sum([e[1] for e in item_set])
        set_value = sum([e[2] for e in item_set])
        if set_value > best_value and set_weight <= max_weight:
            best_value = set_value
            best_weight = set_weight
            knapsack = item_set
    for i in knapsack:
        ids = [i[0]] +ids
    return ids, best_weight, best_value

def dynamicKnapSack(W, items, n):
    V = []

    for i in range(n + 1):
        V.append([0] * (W + 1))

    for i in range(1, n + 1): 
        for w in range(W + 1): 
            if (items[i - 1][1] > w):
                V[i][w] = V[i - 1][w]
            elif (items[i - 1][2] + V[i - 1][w - items[i - 1][1]] > V[i - 1][w]):
                V[i][w] = items[i - 1][2] + V[i - 1][w - items[i - 1][1]]
            else: 
                V[i][w] = V[i - 1][w]
    return V


def findElements(V,W,n,items):
    k = W
    peso= 0
    elements = []
    for i in range(n, 0, -1):
        if (V[i][k] != V[i - 1][k]):
            elements.append(i)
            i -= 1
            peso = peso+items[i][1]
            k -= items[i][1]
        else:
            i -= 1
    
    return [elements,peso]


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
    includeItems= "Incluidos: "
    for i in range(len(wt)):
        if(TEST(msk,i)):
            includeItems = includeItems + str(i) +","
    print(includeItems[:len(includeItems)-1])

def generateMemo(n,m):
    mn = []
    for _ in range(n):
        fila = [0 for i in range(m)]
        mn.append(fila)
    return mn   

def setFormat(items):
    values = [0]
    weigth = [0]
    for i in items:
        values = values+ [i[2] ]
        weigth = weigth +[i[1]]
    return weigth, values
###############################################################################

#items = [[1,5,20], [2,15,50], [3,10,60],[4,10,62],[5, 8, 40]]


#print(setFormat(items))
main(sys.argv)
'''n = 30
wt = [0, 5, 15, 10, 10, 8]
val =  [0, 20, 50, 60, 62, 40]
memo = generateMemo(len(val),n+1)
print(topDownKnapsack(len(val)-1, n, memo))
#for i in memo:
#    print(i)

printChoosen((choosenItems(memo)))'''
#
