import csv

class MenuOlimpiadas:

    def menu(self):
        opcion = input('''Elige la operacion que quieres realizar :
        1- Generar fichero CSV de olimpiadas
        2- Buscar deportista
        3- Buscar deportista por deporte y olimpiada
        4- Añadir deportista
        ''')
        if opcion == "1":
            self.generarCSV()



    def generarCSV(self):
        # El archivo CSV para lectura
        archivoEntrada = "athlete_events.csv"

        # Nombre del nuevo archivo CSV
        archivOlimpiadas = "olimpiadas.csv"

        # Los campos Games, Year, Season y City pa extraer
        campos = ["Games", "Year", "Season", "City"]

        # Lee el archivo CSV de entrada y crea un nuevo archivo CSV
        with open(archivoEntrada, mode="r", newline="") as entrada, open(archivOlimpiadas, mode="w", newline="") as salida:
            # Creación de las variables para leer y escribir
            lecturaCsv = csv.DictReader(entrada)
            escrituraCsv = csv.DictWriter(salida)
            # Escribir la cabecera con los campos en el archivo salida
            escrituraCsv.writeheader()
            # iteramos sobre el archivo csv y metemos en el nuevo archivo los datos queridos en forma []
            for fila in lecturaCsv:
                nuevaFila = []
                for campo in campos:
                    nuevaFila.append(fila[campo])
                    escrituraCsv.writerow(nuevaFila)
            print("PERFECTO")

M1 = MenuOlimpiadas()
M1.menu()