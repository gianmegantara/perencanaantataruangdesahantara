import random
import csv

jumlahGen = 5
jumlahKromosom = 5
mutationRate = 0.1

def loadCsv():
    array = []
    direktori = open('../data.csv','r')
    reader = csv.reader(direktori)
    for row in reader:
        array.insert(0,row)
    return array

data = loadCsv()

def inisialisasiPopulasi():
    populasi = []
    for j in range(jumlahKromosom):
        array = []
        randomgen = random.sample(range(0,29), jumlahGen)
        for i in randomgen:
            datarandom = data[i]
            array.insert(0,datarandom)
        populasi.insert(0,array)
    return populasi

populasi = inisialisasiPopulasi()

print('POPULASI')
for i in range(len(populasi)):
    print(populasi[i])

def evaluateFitness():
    individuFitness = []
    for i in range(jumlahKromosom):
        kromosom =[]
        fitness = 0
        for j in range(jumlahKromosom):
            for k in range(1):
                if populasi[i][j][3] == 'Hutan':
                    fitness = fitness + 1
                elif populasi[i][j][3] == 'Sawah Irigasi':
                    fitness = fitness + 1
                elif populasi[i][j][3] == 'Pemukiman':
                    fitness = fitness + 1
            kromosom.insert(4,populasi[i][j])
        kromosom.insert(0, 1-fitness/jumlahKromosom)
        individuFitness.insert(0,kromosom)
    return individuFitness

individuFitness = evaluateFitness()
individuFitness.sort()

print('FITNESS INDIVIDU')
for i in range(len(individuFitness)):
    print('fitness individu',i,individuFitness[i])

def crossoverKromosom():
    parent = individuFitness[3:5]

    parent1 = parent[0][1:6]
    parent2 = parent[1][1:6]

    children =[]
    child1 = []
    child1.insert(0,parent2[0])
    child1.insert(1,parent2[1])
    child1.insert(2,parent1[2])
    child1.insert(3,parent1[3])
    child1.insert(4,parent1[4])

    child2 = []
    child2.insert(0,parent1[0])
    child2.insert(1,parent1[1])
    child2.insert(2,parent2[2])
    child2.insert(3,parent2[3])
    child2.insert(4,parent2[4])

    children.insert(0,child1)
    children.insert(1,child2)

    return children

children = crossoverKromosom()
print('ANAK')
for i in range(len(children)):
    print('anak',i,children[i])

def mutation():
    mutant = []
    mutant1 = children[0]
    mutant2 = children[1]
    for i in range(jumlahKromosom):
        randomValue = random.random()
        randomData = random.randint(0,29)
        if randomValue <= mutationRate:
            mutant1[i] = data[randomData]
    for i in range(jumlahKromosom):
        randomValue = random.random()
        randomData = random.randint(0,29)
        if randomValue <= mutationRate:
            mutant2[i] = data[randomData]

    mutant.insert(0,mutant1)
    mutant.insert(1,mutant2)

    return mutant

mutant = mutation()
print('MUTANT')
for i in range(len(mutant)):
    print('mutant',i,mutant[i])

def regeneration():
    fitnessMutant = []
    for i in range(len(mutant)):
        arrayMutant = []
        fitness = 0
        for j in range(len(mutant[i])):
            for k in range(1):
                if mutant[i][j][3] == 'Hutan':
                    fitness = fitness + 1
                elif mutant[i][j][k] == 'Sawah Irigasi':
                    fitness = fitness + 1
                elif mutant[i][j][3] == 'Pemukiman':
                    fitness = fitness + 1
            arrayMutant.insert(4,mutant[i][j])
        arrayMutant.insert(0, 1-fitness/jumlahKromosom)
        fitnessMutant.insert(0,arrayMutant)
    individuFitness.insert(5,fitnessMutant[0])
    individuFitness.insert(6,fitnessMutant[1])
    print('generasi baru')
    individuFitness.sort()
    del individuFitness[0:2]
    for i in range(len(individuFitness)):
        print(individuFitness[i])

newGeneration = regeneration()

for i in range(100):
    mutation()
    regeneration()
    for j in range(1):
        inisialisasiPopulasi()
        evaluateFitness()
        crossoverKromosom()





