import random, csv

jumlahKromosom = 4
jumlahGen = 4
crossoverRate = 1
mutationRate = 0.5
totalPelanggaran = 0
DataProyeksi = 0

def loadCsv():
    array = []
    arrayProyeksi = []
    direktori = open('../datafixlastest.csv','r')
    reader = csv.reader(direktori)
    for row in reader:
        array.insert(len(array),row)
        arrayProyeksi.insert(len(arrayProyeksi),row)
    global DataProyeksi
    DataProyeksi = arrayProyeksi
    return array
Data = loadCsv()
print("Banyak Data",len(Data))

def inisialisasiPopulasi():
    populasi = []
    for j in range(jumlahKromosom):
        array = []
        randomgen = random.sample(range(0, (len(Data) - 1)), jumlahGen)
        for i in randomgen:
            datarandom = Data[i]
            array.insert(len(array), datarandom)
        populasi.insert(len(populasi), array)
    return populasi
populasi = inisialisasiPopulasi()
print("POPULASI")
for i in range(len(populasi)):
    print("Kromosom", i)
    for j in range(len(populasi[i])):
        print(populasi[i][j])
print()
print("#"*1000)

def evaluasiFitness():
    fitnessKromosom = []
    for i in range(jumlahKromosom):
        kromosom = []
        fitness = 0
        for j in range(jumlahGen):
            for k in range(1):
                if populasi[i][j][3] == 'Hutan':
                    fitness += 1
                    if populasi[i][j] in Data:
                        Data.remove(populasi[i][j])
                elif populasi[i][j][3] == 'SawahIrigasi':
                    fitness += 1
                    if populasi[i][j] in Data:
                        Data.remove(populasi[i][j])
                elif populasi[i][j][3] == 'Pemukiman':
                    fitness += 1
                    if populasi[i][j] in Data:
                        Data.remove(populasi[i][j])
            kromosom.insert(0, populasi[i][j])
        kromosom.insert(0, 1 - fitness / jumlahGen)
        kromosom.insert(1, fitness)
        fitnessKromosom.insert(0, kromosom)
    return fitnessKromosom
fitnessKromosom = evaluasiFitness()
fitnessKromosom.sort()
print()
print("FITNESS POPULASI")
for i in range(len(fitnessKromosom)):
    print("INDIVIDU")
    for j in range(len(fitnessKromosom[i])):
        print(fitnessKromosom[i][j])
print()
print("#"*1000)

nilai = 0
iteration = 1
while nilai < 1:

    print("CROSSOVER")
    def crossoverKromosom():
        randomValue = random.random()
        parent = fitnessKromosom[jumlahKromosom - 2:jumlahKromosom]
        parent1 = parent[0][2:]
        parent2 = parent[1][2:]
        print("PARENT 1")
        for i in range(len(parent1)):
            print(parent1[i])
        print("PARENT 2")
        for i in range(len(parent2)):
            print(parent2[i])
        if randomValue <= crossoverRate:
            lenParent1 = round(len(parent1) / 2)
            lenParent2 = round(len(parent2) / 2)
            children = []
            child1 = []
            for i in range(0, lenParent1):
                child1.insert(i, parent2[i])
            for i in range(lenParent1, len(parent1)):
                child1.insert(i, parent1[i])
            child2 = []
            for i in range(0, lenParent2):
                child2.insert(i, parent1[i])
            for i in range(lenParent2, len(parent2)):
                child2.insert(i, parent2[i])
            children.insert(0, child1)
            children.insert(1, child2)
            return children
        else:
            children = []
            children.insert(0, parent1)
            children.insert(1, parent2)
            return children
    children = crossoverKromosom()
    print("CHILDREN")
    for i in range(len(children)):
        print("CHILD", i)
        for j in range(len(children[i])):
            print(children[i][j])
    print()
    print("#"*1000)
    print()

    def mutasiKromosom():
        mutant = []
        mutant1 = children[0]
        mutant2 = children[1]
        for i in range(jumlahGen):
            randomValue = random.random()
            randomData = random.randint(0, (len(Data) - 1))
            if randomValue <= mutationRate:
                if Data[randomData] in mutant1:
                    continue
                else:
                    mutant1[i] = Data[randomData]
        for i in range(jumlahGen):
            randomValue = random.random()
            randomData = random.randint(0, (len(Data) - 1))
            if randomValue <= mutationRate:
                if Data[randomData] in mutant2:
                    continue
                else:
                    mutant2[i] = Data[randomData]
        mutant.insert(0, mutant1)
        mutant.insert(1, mutant2)
        return mutant
    mutant = mutasiKromosom()
    print("MUTASI")
    for i in range(len(mutant)):
        print("MUTANT", i)
        for j in range(len(mutant[i])):
            print(mutant[i][j])
    print('GENERASI', iteration)
    def regenerasi():
        fitnessMutant = []
        pelanggaran = 0
        for i in range(len(mutant)):
            arrayMutant = []
            fitness = 0
            for j in range(len(mutant[i])):
                for k in range(1):
                    if mutant[i][j][3] == 'Hutan':
                        fitness += 1
                        if mutant[i][j] in Data:
                            Data.remove(mutant[i][j])
                    elif mutant[i][j][3] == 'SawahIrigasi':
                        fitness += 1
                        if mutant[i][j] in Data:
                            Data.remove(mutant[i][j])
                    elif mutant[i][j][3] == 'Pemukiman':
                        fitness += 1
                        if mutant[i][j] in Data:
                            Data.remove(mutant[i][j])
                arrayMutant.insert(0, mutant[i][j])
            arrayMutant.insert(0, 1 - fitness / jumlahGen)
            arrayMutant.insert(1, fitness)
            fitnessMutant.insert(0, arrayMutant)
        fitnessKromosom.insert(len(fitnessKromosom) - 1, fitnessMutant[0])
        fitnessKromosom.insert(len(fitnessKromosom) - 2, fitnessMutant[1])
        fitnessKromosom.sort()
        del fitnessKromosom[0:2]
        for i in range(len(fitnessKromosom)):
            print('Kromosom', i)
            for j in range(len(fitnessKromosom[i])):
                print(fitnessKromosom[i][j])
            pelanggaran += fitnessKromosom[i][1]
        global totalPelanggaran
        totalPelanggaran += pelanggaran
        return fitnessKromosom

    newGeneration = regenerasi()

    if fitnessKromosom[len(fitnessKromosom)-1][0] >= 1.0:
        nilai = 2
    iteration += 1