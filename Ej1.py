#!/usr/bin/env python3
import json
import os

archivoJson = "datos.json"
personas=[]

# Comprueba si el archivo JSON ya existe
if not os.path.exists(archivoJson):
    # El archivo no existe, así que lo creamos
    with open(archivoJson, "w") as nuevo_archivo_json:
        # No escribimos ningún contenido en el archivo en este caso
        pass
    print("Archivo JSON creado.")
else:
    print("El archivo JSON ya existe, no se realizó ninguna escritura.")


class Persona:
    def __init__(self,dni,nombre,edad):
        self.dni=dni
        self.nombre=nombre
        self.edad=edad
    def aDiccionario(self):
        return{
            "dni":self.dni,
            "nombre":self.nombre,
            "edad":self.edad
        }
def mostrar_menu():
    print("Menú:")
    print("1. Crear C")
    print("2. Borrar D")
    print("3. modificar U")
    print("4. Leer R")
    print("5. Salir")

def cargar_array1():
    with open("datos.json", "r") as archivo:
        try:
            diccionario = json.load(archivo)
        except(json.decoder.JSONDecodeError):
            print("no hay datos")
            diccionario={}
        for d in diccionario:
            p1 = Persona(d.get("dni"),d.get("nombre"),d.get("edad"))
            personas.append(p1)

def crear():
    dni=input("Introduce un dni: ")
    nombre=input("Introduce edad: ")
    edad=input("Introduce la edad: ") 
    p1=Persona(dni,nombre,edad)
    personas.append(p1)

def borrar():
    b1=input("Introduce el dni de la persona que desea borrar: ")
    for p in personas:
        if p.dni ==b1:
            personas.remove(p)
            print("Borrado correctamente")
    

def guardarJson2(personas):
    personas=[p.aDiccionario()for p in personas]
    archivo=open("datos.json","w")
    data=json.dumps(personas)
    archivo.write(data)
    archivo.close

def seleccion():
    while True:
        mostrar_menu()
        opc=input('Elige una opcion CRUD o salir(S)')
        
        match opc:
            case 'c':
                crear()

            case 'r':
                print
            case 'u':
                print
            case 'd':
                borrar()
                print
            case 's':
                guardarJson2(personas)
                break
            case other:
                print("Opción no válida. Por favor, selecciona una opción válida.")
cargar_array1()
seleccion()

