#!/usr/bin/env python3
import fechas
from datetime import datetime
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
    def __init__(self,dni,nombre,edad,fechaNac):
        self.dni=dni
        self.nombre=nombre
        self.edad=edad
        self.fechaNac=fechaNac
    def aDiccionario(self):
        return{
            "dni":self.dni,
            "nombre":self.nombre,
            "edad":self.edad,
            "fechaNac":self.fechaNac
        }
    def __str__(self):
        fechaFin=datetime.fromtimestamp(self.fechaNac).strftime('%Y-%m-%d')
        return f'La persona con dni {self.dni} se llama {self.nombre} y tiene {self.edad} años y nacio en {fechaFin}'
        
def mostrar_menu():
    print("Menú:")
    print("1. Crear C")
    print("2. Borrar D")
    print("3. modificar U")
    print("4. Leer R")
    print("5. Leer fecha")
    print("6. Salir")

def cargar_array1():
    with open("datos.json", "r") as archivo:
        try:
            diccionario = json.load(archivo)
        except(json.decoder.JSONDecodeError):
            print("no hay datos")
            diccionario={}
        for d in diccionario:
            p1 = Persona(d.get("dni"),d.get("nombre"),d.get("edad"),d.get("fechaNac"))
            personas.append(p1)

def crear():
    print("Dentro de crear")
    dni=input("Introduce un dni: ")
    nombre=input("Introduce el nombre ")
    edad=input("Introduce la edad: ")
    fechaNac=fechas.leerFechaValida()
    p1=Persona(dni,nombre,edad,fechaNac)
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

def buscar(personas):
    personaCambio=None
    x=input("Introduce un dni: ")
    for p in personas:
        if x == p.dni:
            print("Encontrado")

            print(str(p))
            personaCambio=p
    if personaCambio == None:
        print("No se ha encontrado niguna persona con ese dni ")
def actualizar(personas):
    personaCambio=None
    x=input("Introduce un dni: ")
    for p in personas:
        if x == p.dni:
            print("Encontrado")
            personaCambio=p
    if personaCambio!=None:
        print(str(p))
        opc1=input("cambiar dni: d, cambiar edad: e, cambiar nombre: n\n")
        match opc1:
                case 'd':
                    dni=input("Introduce el nuevo dni: ")
                    personaCambio.dni=dni
                case 'e':
                    edad=input("Introduce la nueva edad: ")
                    personaCambio.edad=edad
                case 'n':
                    nombre=input("Introduce el nuevo nombre: ")
                    personaCambio.nombre=nombre
    else:
        print("No se ha encontrado niguna persona con ese dni ")
def borrar(personas):
    personaCambio=None
    x=input("Introduce un dni: ")
    for p in personas:
        if x == p.dni:
            print("Encontrado")
            personaCambio=p
    if personaCambio!=None:
        personas.remove(personaCambio)
    else:
        print("No se ha encontrado niguna persona con ese dni ")

def seleccion():
    while True:
        mostrar_menu()
        opc=input('Elige una opcion CRUD o salir(S)')
        
        match opc:
            case 'c':
                crear()
                guardarJson2(personas)
            case 'r':
                buscar(personas)
            case 'u':
                actualizar(personas)
                guardarJson2(personas)
                print
            case 'd':
                borrar(personas)
                guardarJson2(personas)
                print
            case 's':
                break
            case other:
                print("Opción no válida. Por favor, selecciona una opción válida.")
cargar_array1()
seleccion()