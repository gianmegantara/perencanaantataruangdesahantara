from tkinter import Tk, ttk, Label, LabelFrame, Button, Entry, PanedWindow, Frame, N, NW, W, HORIZONTAL, filedialog, StringVar
from geojson import Polygon, Feature, FeatureCollection, dump
import csv, random, webbrowser

DataExport = []
DataProyeksi = 0
Data = 0
jumlahGen = 0
jumlahKromosom = 0
crossoverRate = 0
mutationRate = 0
totalPelanggaran = 0

class View:
    def __init__(self, master):
        self.master = master
        self.master.title("Skripsi_2014081062 2.0")
        self.master.iconbitmap("love.ico")
        self.content = ttk.Frame(root, padding=(20, 10, 20, 20))
        self.content.grid(column=0, row=0)
        self.titleLabel = ttk.Label(self.content, text="Aplikasi Perencanaan Tata Ruang dengan Algoritma Genetika", font="Arial 12 bold")
        self.titleLabel.grid(column=0, row=0, columnspan=5, sticky=(N), padx=20, pady=20)
        self.buttonOpen = ttk.Button(self.content, text="Impor Data", command=self.importData)
        self.buttonOpen.grid(column=0, row=1, sticky=(W))
        self.panel = ttk.PanedWindow(self.content, orient=HORIZONTAL)
        self.panel.grid(column=0, row=3, sticky=(NW), pady=20)
        self.panelProyeksiPenduduk = ttk.LabelFrame(self.panel, text="Proyeksi Penduduk")
        self.panel.add(self.panelProyeksiPenduduk)
        self.labelDataPenThDasar = ttk.Label(self.panelProyeksiPenduduk, text="Masukkan data Penduduk pada tahun Dasar:")
        self.labelDataPenThDasar.grid(column=0, row=0, sticky=(W), padx=10)
        self.dataPenThDasar = StringVar()
        self.entryDataPenThDasar = ttk.Entry(self.panelProyeksiPenduduk, textvariable=self.dataPenThDasar)
        self.entryDataPenThDasar.grid(column=0, row=1, sticky=(W), padx=12, pady=10)
        self.dataPenThAkhir = ttk.Label(self.panelProyeksiPenduduk, text="Masukkan data Penduduk pada tahun Akhir:")
        self.dataPenThAkhir.grid(column=0, row=2, sticky=(W), padx=10)
        self.dataPenThAkhir = StringVar()
        self.entryDataPenThAkhir = ttk.Entry(self.panelProyeksiPenduduk, textvariable=self.dataPenThAkhir)
        self.entryDataPenThAkhir.grid(column=0, row=3, sticky=(W), padx=12, pady=10)
        self.labelSelisihThDasardanAkhir = ttk.Label(self.panelProyeksiPenduduk, text="Masukkan selisih Tahun Dasar dan Akhir:")
        self.labelSelisihThDasardanAkhir.grid(column=0, row=4, sticky=(W), padx=10)
        self.selisihThDasardanAkhir = StringVar()
        self.entrySelisihThDasardanAkhir = ttk.Entry(self.panelProyeksiPenduduk, textvariable=self.selisihThDasardanAkhir)
        self.entrySelisihThDasardanAkhir.grid(column=0, row=5, sticky=(W), padx=12, pady=10)
        self.labelSelisihThProyeksidanAkhir = ttk.Label(self.panelProyeksiPenduduk, text="Masukkan selisih Tahun Proyeksi dan Akhir:")
        self.labelSelisihThProyeksidanAkhir.grid(column=0, row=6, sticky=(W), padx=10)
        self.selisihThProyeksidanAkhir = StringVar()
        self.entrySelisihThProyeksidanAkhir = ttk.Entry(self.panelProyeksiPenduduk, textvariable=self.selisihThProyeksidanAkhir)
        self.entrySelisihThProyeksidanAkhir.grid(column=0, row=7, sticky=(W), padx=12, pady=10)
        self.buttonHitungProyeksi = ttk.Button(self.panelProyeksiPenduduk, text="Hitung Proyeksi", command= self.hitungProyeksiPenduduk)
        self.buttonHitungProyeksi.state(["disabled"])
        self.buttonHitungProyeksi.grid(column=0, row=8, sticky=(W), padx=12, pady=10)
        self.labelHasilProyeksi = ttk.Label(self.panelProyeksiPenduduk, text="Hasil Proyeksi Penduduk adalah : ")
        self.labelHasilProyeksi.grid(column=0, row=9, sticky=(W), padx=12)
        self.hProyeksi = StringVar()
        self.labelHProyeksi = ttk.Label(self.panelProyeksiPenduduk, textvariable=self.hProyeksi)
        self.labelHProyeksi.grid(column=0, row=10, sticky=(W), padx=12, pady=10)
        self.panelParameterAG = ttk.LabelFrame(self.panel, text="Parameter Algoritma Genetika")
        self.panel.add(self.panelParameterAG)
        self.labelPanelParameterAG = ttk.Label(self.panelParameterAG, text="Jumlah Gen penyelesaian yang dibutuhkan: ")
        self.labelPanelParameterAG.grid(column=0, row=0, sticky=(W), padx=10)
        self.genDibutuhkan = StringVar()
        self.labelGenDibutuhkan = ttk.Label(self.panelParameterAG, textvariable=self.genDibutuhkan)
        self.labelGenDibutuhkan.grid(column=0, row=1, sticky=(W), padx=10)
        self.labelJumlahKromosom = ttk.Label(self.panelParameterAG, text="Masukan Jumlah Kromosom dalam satu generasi: ")
        self.labelJumlahKromosom.grid(column=0, row=2, sticky=(W), padx=10)
        self.jmlKromosom = StringVar()
        self.entryJumlahKromosom = ttk.Entry(self.panelParameterAG, textvariable=self.jmlKromosom)
        self.entryJumlahKromosom.grid(column=0, row=3, sticky=(W), padx=12, pady=10)
        self.labelPCrossover = ttk.Label(self.panelParameterAG, text="Masukan Probabilitas Crossover (0-1): ")
        self.labelPCrossover.grid(column=0, row=4, sticky=(W), padx=10)
        self.probCrosover = StringVar()
        self.entryPCrossover = ttk.Entry(self.panelParameterAG, textvariable = self.probCrosover)
        self.entryPCrossover.grid(column=0, row=5, sticky=(W), padx=12, pady=10)
        self.labelPMutasi = ttk.Label(self.panelParameterAG, text="Masukan Probabilitas Mutasi (0-1): ")
        self.labelPMutasi.grid(column=0, row=6, sticky=(W), padx=10)
        self.probMutasi = StringVar()
        self.entryPMutasi = ttk.Entry(self.panelParameterAG, textvariable = self.probMutasi)
        self.entryPMutasi.grid(column=0, row=7, sticky=(W), padx=12, pady=10)
        self.buttonHitungAlgoritmaGenetika = ttk.Button(self.panelParameterAG, text="Hitung dengan AG", command=self.hitungAlgoritmaGenetika)
        self.buttonHitungAlgoritmaGenetika.state(["disabled"])
        self.buttonHitungAlgoritmaGenetika.grid(column=0, row=8, sticky=(W), padx=12, pady=10)
        self.buttonSimpan = ttk.Button(self.panelParameterAG, text="Simpan Data",command=self.simpanData)
        self.buttonSimpan.state(["disabled"])
        self.buttonSimpan.grid(column=0, row=9, sticky=(W), padx=12, pady=10)
        self.panelVisualisasi = ttk.LabelFrame(self.panel, text="Visualisasi")
        self.panel.add(self.panelVisualisasi)
        self.buttonVisualisasiAwal = ttk.Button(self.panelVisualisasi, text="Visualisasi Awal", command=self.visualisasiAwal)
        self.buttonVisualisasiAwal.state(['disabled'])
        self.buttonVisualisasiAwal.grid(column=0, row=0, sticky=(W), padx=12, pady=10)
        self.buttonVisualisasiProyeksi = ttk.Button(self.panelVisualisasi, text="Visualisasi Proyeksi", command=self.visualisasiProyeksi)
        self.buttonVisualisasiProyeksi.state(['disabled'])
        self.buttonVisualisasiProyeksi.grid(column=0, row=2, sticky=(W), padx=12, pady=10)

    def importData(self):
        direktoriFileImport = filedialog.askopenfilename(filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), title="Choose a file.")
        arrayData = []
        arrayDataProyeksi = []
        file = open(direktoriFileImport)
        if direktoriFileImport is None:
            print('file not imported')
        else:
            reader = csv.reader(file, skipinitialspace=True)
            for row in reader:
                arrayData.insert(len(arrayData), row)
                arrayDataProyeksi.insert(len(arrayDataProyeksi), row)
        global Data
        Data = arrayData
        print(Data)
        print(len(Data))
        self.popupDataTerImpor()

    def popupDataTerImpor(self):
        popup = Tk()
        popup.wm_title("Notifikasi")
        label = ttk.Label(popup, text="Data Berhasil Di-Import")
        label.pack(side="top", fill="x", pady=10, padx=10)
        buttonOK = ttk.Button(popup, text="OK", command=popup.destroy)
        buttonOK.pack(padx=10, pady=10)
        self.buttonHitungProyeksi.state(["!disabled"])
        self.buttonVisualisasiAwal.state(["!disabled"])
        self.buttonHitungAlgoritmaGenetika.state(["disabled"])
        self.buttonSimpan.state(["disabled"])
        self.buttonVisualisasiProyeksi.state(["disabled"])
        popup.mainloop()

    def hitungProyeksiPenduduk(self):
        def valueError():
            popup = Tk()
            popup.wm_title("Perhatian !!")
            label = ttk.Label(popup, text="Periksa Kembali Nilai Inputan Proyeksi Penduduk")
            label.pack(side="top", fill="x", pady=10, padx=10)
            buttonOK = ttk.Button(popup, text="OK", command=popup.destroy)
            buttonOK.pack(padx=10, pady=10)
            popup.mainloop()

        global jumlahGen
        try:
            dataPenThAkhir = int(self.dataPenThAkhir.get())
            dataPenThDasar = int(self.dataPenThDasar.get())
            selisihThDasardanAkhir = int(self.selisihThDasardanAkhir.get())
            selisihThProyeksidanAkhir = int(self.selisihThProyeksidanAkhir.get())
            try:
                if dataPenThAkhir and dataPenThDasar and selisihThDasardanAkhir and selisihThProyeksidanAkhir:
                    int(dataPenThAkhir and dataPenThDasar and selisihThDasardanAkhir and selisihThProyeksidanAkhir)
                rataPertambahan = round((dataPenThAkhir - dataPenThDasar) / selisihThDasardanAkhir)
                proyeksiPenduduk = round(dataPenThAkhir + (selisihThProyeksidanAkhir * rataPertambahan))
            except ValueError:
                valueError()
            self.hProyeksi.set(proyeksiPenduduk)
            lahanDibutuhkan = round((proyeksiPenduduk - dataPenThAkhir) / 3.41)
            if lahanDibutuhkan >= 8400:
                valueError()
            jumlahGen = lahanDibutuhkan
            self.genDibutuhkan.set(lahanDibutuhkan)
            self.buttonHitungProyeksi.state(["disabled"])
            self.buttonHitungAlgoritmaGenetika.state(["!disabled"])
        except ValueError:
            valueError()

    def hitungAlgoritmaGenetika(self):
        def valueError():
            popup = Tk()
            popup.wm_title("Perhatian !!")
            label = ttk.Label(popup, text="Periksa Kembali Nilai Inputan Parameter Algoritma")
            label.pack(side="top", fill="x", pady=10, padx=10)
            button = ttk.Button(popup, text="OK", command=popup.destroy)
            button.pack(padx=10, pady=10)
            popup.mainloop()
        global jumlahKromosom, crossoverRate, mutationRate, Data
        self.buttonSimpan.state(["!disabled"])
        try:
            jumlahKromosom = int(self.jmlKromosom.get())
            crossoverRate = float(self.probCrosover.get())
            mutationRate = float(self.probMutasi.get())
            try:
                if jumlahKromosom:
                    int(jumlahKromosom)
                    if crossoverRate >=0 and crossoverRate <=1:
                        float(crossoverRate)
                    else:
                        valueError()
                    if mutationRate >=0 and mutationRate <=1:
                        float(mutationRate)
                    else:
                        valueError()
                algoritmaGenetika = AlgoritmaGenetika(jumlahGen, jumlahKromosom, crossoverRate, mutationRate, Data)
            except ValueError:
                valueError()
        except ValueError:
            valueError()

    def popupPerhitunganSelesai(self):
        popup = Tk()
        popup.wm_title("Notifikasi")
        label = ttk.Label(popup, text="Perhitungan Telah Selesai")
        label.pack(side="top", fill="x", pady=10, padx=10)
        buttonOK = ttk.Button(popup, text="OK", command=popup.destroy)
        buttonOK.pack(padx=10, pady=10)
        popup.mainloop()

    def simpanData(self):
        def valueError():
            popup = Tk()
            popup.wm_title("Perhatian !!")
            label = ttk.Label(popup, text="Periksa Kembali perhitungan Algoritma")
            label.pack(side="top", fill="x", pady=10, padx=10)
            buttonOK = ttk.Button(popup, text="OK", command=popup.destroy)
            buttonOK.pack(padx=10, pady=10)
            popup.mainloop()
        dataProyeksi = DataExport
        if dataProyeksi == []:
            valueError()
        features = []
        for i in range(len(dataProyeksi)):
            koordinat = Polygon((dataProyeksi[i]))
            features.append(Feature(geometry= koordinat))
        features_collection = FeatureCollection(features)
        with open('C:/xampphp5/htdocs/proyeksi/geojson/proyeksi/proyeksi.geojson', 'w') as f:
            dump(features_collection, f)
        self.popupDataTersimpan()

    def popupDataTersimpan(self):
        popup = Tk()
        popup.wm_title("Notifikasi")
        label = ttk.Label(popup, text="Data Berhasil Di-Simpan")
        label.pack(side="top", fill="x", pady=10, padx=10)
        buttonOK = ttk.Button(popup, text="OK", command=popup.destroy)
        buttonOK.pack(padx=10, pady=10)
        self.buttonHitungAlgoritmaGenetika.state(["disabled"])
        self.buttonVisualisasiProyeksi.state(["!disabled"])
        self.buttonSimpan.state(["disabled"])
        popup.mainloop()

    def visualisasiProyeksi(self):
        self.url = "http://localhost/proyeksi/mappingproyeksi.html"
        webbrowser.open_new(self.url)

    def visualisasiAwal(self):
        self.url = "http://localhost/proyeksi/mappingdasar.html"
        webbrowser.open_new(self.url)

class AlgoritmaGenetika:
    def __new__(self, jumlahGen, jumlahKromosom, crossoverRate, mutationRate, Data):
        self.jumlahGen = jumlahGen
        self.jumlahKromosom = jumlahKromosom
        self.crossoverRate = crossoverRate
        self.mutationRate = mutationRate
        self.Data = Data

        def inisialisasiPopulasi():
            populasi = []
            for i in range(self.jumlahKromosom):
                array = []
                randomgen = random.sample(range(0, (len(self.Data) - 1)), self.jumlahGen)
                for j in randomgen:
                    datarandom = self.Data[j]
                    array.insert(0, datarandom)
                populasi.insert(0, array)
            return populasi
        populasi = inisialisasiPopulasi()

        def evaluasiFitness():
            fitnessKromosom = []
            for i in range(self.jumlahKromosom):
                kromosom = []
                fitness = 0
                for j in range(jumlahGen):
                    for k in range(1):
                        if populasi[i][j][3] == 'Hutan':
                            fitness += 1
                            if populasi[i][j] in self.Data:
                                self.Data.remove(populasi[i][j])
                        elif populasi[i][j][3] == 'SawahIrigasi':
                            fitness += 1
                            if populasi[i][j] in self.Data:
                                self.Data.remove(populasi[i][j])
                        elif populasi[i][j][3] == 'Pemukiman':
                            fitness += 1
                            if populasi[i][j] in self.Data:
                                self.Data.remove(populasi[i][j])
                    kromosom.insert(0, populasi[i][j])
                kromosom.insert(0, 1 - fitness / self.jumlahGen)
                kromosom.insert(1, fitness)
                fitnessKromosom.insert(0, kromosom)
            return fitnessKromosom
        fitnessKromosom = evaluasiFitness()
        fitnessKromosom.sort()

        nilai = 0
        iteration = 1

        while nilai < 1:
            logTemporary = []
            def crossoverKromosom():
                randomValue = random.random()
                parent = fitnessKromosom[self.jumlahKromosom - 2:self.jumlahKromosom]
                parent1 = parent[0][2:]
                parent2 = parent[1][2:]
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

            def mutasiKromosom():
                mutant = []
                mutant1 = children[0]
                mutant2 = children[1]
                for i in range(jumlahGen):
                    randomValue = random.random()
                    randomData = random.randint(0, (len(self.Data) - 1))
                    if randomValue <= mutationRate:
                        if self.Data[randomData] in mutant1:
                            continue
                        else:
                            mutant1[i] = self.Data[randomData]
                for i in range(jumlahGen):
                    randomValue = random.random()
                    randomData = random.randint(0, (len(self.Data) - 1))
                    if randomValue <= mutationRate:
                        if self.Data[randomData] in mutant2:
                            continue
                        else:
                            mutant2[i] = self.Data[randomData]
                mutant.insert(0, mutant1)
                mutant.insert(1, mutant2)
                return mutant
            mutant = mutasiKromosom()

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
                                if mutant[i][j] in self.Data:
                                    self.Data.remove(mutant[i][j])
                            elif mutant[i][j][3] == 'SawahIrigasi':
                                fitness += 1
                                if mutant[i][j] in self.Data:
                                    self.Data.remove(mutant[i][j])
                            elif mutant[i][j][3] == 'Pemukiman':
                                fitness += 1
                                if mutant[i][j] in self.Data:
                                    self.Data.remove(mutant[i][j])
                        arrayMutant.insert(0, mutant[i][j])
                    arrayMutant.insert(0, 1 - fitness / self.jumlahGen)
                    arrayMutant.insert(1, fitness)
                    fitnessMutant.insert(0, arrayMutant)
                fitnessKromosom.insert(len(fitnessKromosom) - 1, fitnessMutant[0])
                fitnessKromosom.insert(len(fitnessKromosom) - 2, fitnessMutant[1])
                fitnessKromosom.sort()
                del fitnessKromosom[0:2]
                for i in range(len(fitnessKromosom)):
                    print('Kromosom', i, fitnessKromosom[i])
                    pelanggaran += fitnessKromosom[i][1]
                logTemporary.insert(1, pelanggaran)
                print('pelanggaran satu generasi : ', pelanggaran)
                global totalPelanggaran
                totalPelanggaran += pelanggaran
                return fitnessKromosom

            newGeneration = regenerasi()

            print('total Pelanggaran ', totalPelanggaran)
            print('rata-rata pelanggaran ', totalPelanggaran / (iteration + 1),"\n")
            if fitnessKromosom[self.jumlahKromosom - 1][0] >= 1.0:
                nilai = 2
            iteration += 1
        del fitnessKromosom[(len(fitnessKromosom) - 1)][0]
        del fitnessKromosom[(len(fitnessKromosom) - 1)][0]
        global DataProyeksi, DataExport
        DataProyeksi = fitnessKromosom[(len(fitnessKromosom) - 1)]
        print(DataProyeksi)
        tmpArrayDataProyeksi = list(DataProyeksi)
        newTmpArrayDataProyeksi = []
        for i in range(len(tmpArrayDataProyeksi)):
            newTmpArrayDataProyeksi.append(tmpArrayDataProyeksi[i][1:3])
        DataExport = []
        for i in range(len(newTmpArrayDataProyeksi)):
            ahiw = []
            newTmpDataExport = []
            for j in range(5):
                newTmpDataExport.append(list(newTmpArrayDataProyeksi[i]))
            ahiw.append(newTmpDataExport)
            DataExport.append(ahiw)
        print(DataExport)
        for i in range(len(DataExport)):
            for j in range(len(DataExport[i])):
                for k in range(len(DataExport[i][j])):
                    if k == 0:
                        DataExport[i][j][k][0] = float(DataExport[i][j][k][0])-0.00003
                        DataExport[i][j][k][1] = float(DataExport[i][j][k][1])-0.00003
                    elif k == 1:
                        DataExport[i][j][k][0] = float(DataExport[i][j][k][0])+0.00003
                        DataExport[i][j][k][1] = float(DataExport[i][j][k][1])-0.00003
                    elif k == 2:
                        DataExport[i][j][k][0] = float(DataExport[i][j][k][0])+0.00003
                        DataExport[i][j][k][1] = float(DataExport[i][j][k][1])+0.00003
                    elif k == 3:
                        DataExport[i][j][k][0] = float(DataExport[i][j][k][0])-0.00003
                        DataExport[i][j][k][1] = float(DataExport[i][j][k][1])+0.00003
                    elif k == 4:
                        DataExport[i][j][k][0] = float(DataExport[i][j][k][0])-0.00003
                        DataExport[i][j][k][1] = float(DataExport[i][j][k][1])-0.00003
        View.popupPerhitunganSelesai(self)

root = Tk()
view = View(root)
root.mainloop()


