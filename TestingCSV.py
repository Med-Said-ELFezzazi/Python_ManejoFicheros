import csv

class Csv:

    def leerArchivo(self):
        fichero = "athlete_events.csv"
        with open(fichero) as csvFile:
            # con csv.DictReader devuelva los datos formato Diccionario con solo reader formato []
            reader = csv.reader(csvFile)
            cont = 0
            for ath in reader:
                cont = cont + 1
                print(ath)
            print(cont)

    def crearArchivo(self):
        fichero = "athlete_events.csv"
        with open(fichero) as csvFile:
            reader = csv.reader(csvFile)
            destino = "ath_event.csv"
            with open(destino, "w") as csvPequeno:
                writer = csv.writer(csvPequeno)
                for ath in reader:
                    datos = [ath[0],ath[1]]
                    writer.writerow(datos)

    def crearArchivoDict(self):
        fichero = "athlete_events.csv"
        with open(fichero) as csvFile:
            reader = csv.DictReader(csvFile)
            destino = "ath_event2.csv"
            with open(destino, "w") as csvPequeno:
                camposDeseados = {"Name","Sex","City"}
                writer = csv.DictWriter(csvPequeno, camposDeseados)
                writer.writeheader()
                for ath in reader:
                    writer.writerow(ath)


c = Csv()
#c.leerArchivo()
c.crearArchivoDict()