import random
import csv

genDibutuhkan = 5
kromosomDibutuhkan = 5

def loadCsv():
    array = []
    direktori = open('data.csv','r')
    reader = csv.reader(direktori)
    for row in reader:
        array.insert(0,row)
    return array

data = loadCsv()

def inisialisasiPopulasi():
    populasi = []
    for j in range(kromosomDibutuhkan):
        array = []
        randomgen = random.sample(range(0,29), genDibutuhkan)
        for i in randomgen:
            datarandom = data[i]
            array.insert(0,datarandom)
        populasi.insert(0,array)
    return populasi

populasi = inisialisasiPopulasi()

def evaluateFitness():
    populasi2 = []
    for i in range(5):
        kromosom =[]
        fitness = 0
        for j in range(5):
            for k in range(1):
                if populasi[i][j][3] == 'Hutan':
                    fitness = fitness + 1
                elif populasi[i][j][3] == 'Sawah Irigasi':
                    fitness = fitness + 1
                elif populasi[i][j][3] == 'Pemukiman':
                    fitness = fitness + 1
            kromosom.insert(4,populasi[i][j])
        kromosom.insert(0, 1-fitness/genDibutuhkan)
        populasi2.insert(0,kromosom)
    return populasi2

populasi2 = evaluateFitness()

def crossoverKromosom():
    print('populasi sorted')
    populasi2.sort()
    for i in range(5):
        print(populasi2[i])

    print('parent')
    parent = populasi2[3:5]
    for i in range(2):
        print(parent[i])

    print('parent1')
    parent1 = parent[0]
    print(parent1)
    print('parent2')
    parent2 = parent[1]
    print(parent2)

    print('offspring1')
    offspring1 = []
    offspring1.insert(0,parent2[1:3])
    offspring1.insert(3,parent1[3:6])
    print(offspring1)

    print('offspring2')
    offspring2 = []
    offspring2.insert(0,parent1[1:3])
    offspring2.insert(3,parent2[3:6])
    print(offspring2)







