# Diclaracion de libririas en este eje necesitamos los 2 os y shutil para manipular los files y directorios
import os
import shutil

class Menu:
    def menu(self):
        while True:
            opcion = input('''Elige la operacion que quieres realizar :
            1- Crear un directorio
            2- Listar un directorio
            3- Copiar un archivo
            4- Mover un archivo
            5- Eliminar un archivo/directorio
            6- Salir del programa
            ''')
            if opcion == "1":
                self.crearDir()
            elif opcion == "2":
                self.listarDir()
            elif opcion == "3":
                self.copiarArchivo()
            elif opcion == "4":
                self.moveArchivo()
            elif opcion == "5":
                self.eliArchDir()
            elif opcion == "6":
                print("Adios !")
                break
    def crearDir(self):
        nomDir = input("Introduce el nombre del nuevo directorio a crear :")
        ruta = input("Donde quieres crear el directorio , intoduce la ruta :")
        while os.path.exists(ruta) == False:
            print("La ruta propocionada es incorrecta!")
            ruta = input("Introduce la ruta otra vez :")
        if os.path.exists(ruta) == True:
            barra = "\\"
            rutaFinal = ruta + barra + nomDir
            os.mkdir(rutaFinal)
        return print("El directorio ",nomDir,"ha creado correctamente :)")

    def listarDir(self):
        ruta = input("Introduce la ruta del directorio que quieres listar :")
        while os.path.exists(ruta) == False:
            print("ruta invalida")
            ruta = input("introduce la ruta otra vez :")
        #listdir devuelva una lista de items
        listaItems = os.listdir(ruta)
        print("La ruta introducida tiene lo seguinte :")
        for item in listaItems:
            print(item)


    def checkRuta(self, rutaOrigin, rutaDestino):
        if os.path.exists(rutaOrigin) is True and os.path.exists(rutaDestino) is True:
            return True
        else:
            return False
        # intento de usar un methodo creado by me
        # def moveArchivo(self):
        #     rutaOrigin = input("introduce la ruta original del archivo que quieres mover:")
        #     rutaDestino = input("introduce la ruta distinario : ")
        #     if (checkRuta(rutaOrigin,rutaDestino) = True):

    def copiarArchivo(self):
        rutaOrigin = input("introduce la ruta original del archivo que quieres copiar :")
        # Si la ruta no existe , otra forma os.path.exists(rutaOrigin) == False
        while not os.path.exists(rutaOrigin):
            print("la ruta origin no existe!")
            rutaOrigin = input("introduce la ruta original otra vez :")
        rutaDestino = input("introduce la ruta distinario : ")
        while not os.path.exists(rutaDestino):
            print("la ruta destino no existe!")
            rutaDestino = input("introduce la ruta destino otra vez :")
        if not os.path.isfile(rutaOrigin):
            print("NO es un archivo tiene que ser archivo!")
        else:
            shutil.copy(rutaOrigin, rutaDestino)
            print("se ha copiado el archivo correctamente")

    def moveArchivo(self):
        rutaOrigin = input("introduce la ruta original del archivo que quieres mover:")
        while not os.path.exists(rutaOrigin):
            print("la ruta origin no existe!")
            rutaOrigin = input("introduce la ruta original otra vez :")
        rutaDestino = input("introduce la ruta distinario : ")
        while not os.path.exists(rutaDestino):
            print("la ruta destino no existe!")
            rutaOrigin = input("introduce la ruta destino otra vez :")
        shutil.move(rutaOrigin, rutaDestino)
        return print("se ha movido el archivo correctamente")

    def eliArchDir(self):
        ruta = input("introduce la ruta del archivo/directorio que quieres suprimir:")
        while not os.path.exists(ruta):
            print("la ruta no existe")
            ruta = input("introduce de nuevo la ruta :")
        if os.path.isfile(ruta):
            os.remove(ruta)
            return print("el archivo se ha eliminado correctamente")
        # aqui ponderia directamente else pero como hay muchas funcions isFile isLink ..
        elif os.path.isdir(ruta):
            shutil.rmtree(ruta)
            return print("Se ha suprimido el directorio correctamente ")
        else:
            return print("No existe!")


SistArchivos = Menu()
#print(SistArchivos.checkRuta("/home/dm2/ELpy","/home/dm2/ELpy/subPY"))  FUNCIONA BIEN
SistArchivos.menu()