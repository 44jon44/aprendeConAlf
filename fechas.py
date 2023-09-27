from datetime import datetime

def leerFechaValida():
    
    while True:
        try:
            fecha=input("Introduce una fecha YYYY-MM-DD")
            fecha=datetime.strptime(fecha,'%Y-%m-%d')
            print(fecha.timestamp())
            return fecha.timestamp()
        except ValueError:
            print("Error")

leerFechaValida()
