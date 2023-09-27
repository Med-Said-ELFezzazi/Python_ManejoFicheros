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
        elif opcion == "2":
            self.buscarDeportista()



    def generarCSV(self):
        # El archivo CSV para lectura
        fichero = "athlete_events.csv"
        # Nombre del nuevo archivo CSV
        destino = "olimpiadas.csv"
        # Lee el archivo CSV de entrada y crea un nuevo archivo CSV
        with open(fichero) as csvFile:
            lecturaCsv = csv.reader(csvFile)

            with open(destino, "w") as csvOlimpiadas:
                escrituraCsv = csv.writer(csvOlimpiadas)
                # Escribir la cabecera con los campos en el archivo salida
                #escrituraCsv.writeheader()
                # iteramos sobre el archivo csv y metemos en el nuevo archivo los datos queridos en forma []
                for athleta in lecturaCsv:
                    campos = [athleta[8],athleta[9],athleta[10],athleta[11]]
                    escrituraCsv.writerow(campos)
        return  print("PERFECTO! ha generado el archivo :",destino,"Correctamente")

    def buscarDeportista(self):
        cadenaBusqueda = input("Introduce el nombre del deportista :")
        # Abrimos nuestro fichero
        fichero = "athlete_events.csv"
        listaYaEsta = []
        with open(fichero) as csvFile:
            reader = csv.reader(csvFile)
            for deportista in reader:
                if cadenaBusqueda in deportista[1]:
                    #print("algo")
                    if deportista[0] not in listaYaEsta:
                        listaYaEsta.append(deportista[0])
                        print("El deportista", cadenaBusqueda, "su ID", deportista[0], "Genero", deportista[2], "Edad",deportista[3],"Altura", deportista[4] + " cm Peso", deportista[5], "kg")
                        print("participacion :", deportista[13])
                    elif len(listaYaEsta) == 0:
                        # ESO NO FUNCION TENGO Q REVISARLO LUEGO! "el msg de no existe"
                        print("el deportista no existe")
                    else:
                        print("participacion :", deportista[13])


    def buscarPorDeporteOlimpiada(self):
        deporte = input("Introduce el deporte :").title()
        anio = int(input("Introduce el año :"))
        temporada = input("Introduce la temporada :")
        # Abro el archivo csv
        deportistas = []
        fichero = "athlete_events.csv"
        with open(fichero) as csvFile:
            reader = csv.reader(csvFile)
            cont = 0
            for linea in reader:
                if linea[12] == deporte and int(linea[9]) == anio and linea[10] == temporada:
                    cont += 1
                    if linea[0] not in deportistas:
                        deportistas.append({"nombre": linea[1], "Evento": linea[13], "Medalla": linea[14]})
                        print("La edicion olimpica ,", linea[8], linea[11], "el deporte:", linea[12])
                    else:
                        for deportista in deportistas:
                            print(deportista)
                #print(type(deportistas)) formato lista
            print("hay :", cont)
    #def aniadirDeportista(self):





M1 = MenuOlimpiadas()
M1.buscarPorDeporteOlimpiada()