import random as rand
import sys
from copy import deepcopy
import time
import numpy as np
import itertools

fileName = ""
method = 0
N = 0
max_weight =0
def main(arg):
    global N, max_weight
    if(arg[1]== '1'):
        print("fuerza bruta")
        matrix, origin = processArg(arg)
        for j in range(0, num(N)): # se toma el tiempo
            if origin == 2:
                print("Resultado:")
                print(knapsack_brute_force(matrix,max_weight))

            else:
                print("Resultado:")
                max_weight=matrix[0][0]
                numMatrix = setUpKnapSack(matrix)
                print(knapsack_brute_force(numMatrix,max_weight))
    elif(arg[1] == '2'):
        print("bottom up")
        matrix, origin = processArg(arg)
        for j in range(0, num(N)): # se toma el tiempo
            if origin == 2:
                print("Resultado:")
                V = dynamicKnapSack(max_weight, matrix, len(matrix))
                print(V[len(matrix)][max_weight])
                print(findElements(V, max_weight,len(matrix), matrix))

            else:
                print("Resultado:")
                numMatrix = setUpKnapSack(matrix)
                max_weight=matrix[0][0]
                V = dynamicKnapSack(max_weight, numMatrix, len(numMatrix))
                print(V[len(numMatrix)][max_weight])
                print(findElements(V, max_weight,len(numMatrix), numMatrix))
    elif (arg[1]== '3'):
        print("top-down")   
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


            #proceso los parametros, genero los pesos en una función 
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
    currentMatrix = matrix[1:];
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
    for i in range(n):
        res.append((i, rand.randint(w[0], w[1]), rand.randint(v[0], v[1])))

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


def findElements(V, W, n, items):
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



main(sys.argv)

