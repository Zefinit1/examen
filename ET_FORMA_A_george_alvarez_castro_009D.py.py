import csv
import random
opc = ""
total = 0
promedio = total


nombres = ['Juan Perez', 'Marìa Garcia', 'Carlos Lopez', 'Ana Martinez', 'Pedro Rodriguez', 'Laura Hernandez', 'Miguel Sanchez', 'Isabel Gomez', 'Francisco Diaz', 'Elena Fernandez']

sueldos = random.randint(300000,2500000)
sueldo_menor = []
sueldo_moderado = []
sueldo_alto = []

def asignar_sueldos():
        sueldos = random.randint(300000,2500000)
        nombres = ['Juan Perez', 'Marìa Garcia', 'Carlos Lopez', 'Ana Martinez', 'Pedro Rodriguez', 'Laura Hernandez', 'Miguel Sanchez', 'Isabel Gomez', 'Francisco Diaz', 'Elena Fernandez']  
        print("los sueldos han sido asignados")
        return nombres, sueldos


def clasificar_sueldos():
    
    
    if sueldos in nombres < 800000:
        sueldos.append(sueldo_menor)

    
    if sueldos in nombres > 800000 and sueldos in nombres < 2000000:
        sueldos.append(sueldo_moderado)
    
        
    if sueldos in nombres > 2000000:
        sueldos.append(sueldo_alto)
        
    print("los sueldos fueron clasificados")    
    return sueldos      



def ver_estadisticas():
    print("el sueldo mas alto es", sueldos)
    print("el sueldo mas bajo es", sueldo_menor)
    

    
def reporte_sueldos(examen_csv= 'archivocsv'):
    
    
    with open(examen_csv, 'w', newline='') as archivo:
        campo = ['nombres',sueldos]
        escrito_csv = csv.DictWriter(archivo,fieldnames=campo)
        if archivo.tell()==0:
            
            escrito_csv.writeheader()
            
            escrito_csv.writerow({'Juan Perez' : sueldos,
                                  'Marìa Garcia': sueldos, 
                                  'Carlos Lopez': sueldos, 
                                  'Ana Martinez': sueldos, 
                                  'Pedro Rodriguez': sueldos, 
                                  'Laura Hernandez': sueldos, 
                                  'Miguel Sanchez': sueldos, 
                                  'Isabel Gomez': sueldos, 
                                  'Francisco Diaz': sueldos, 
                                  'Elena Fernandez': sueldos})
        
    
    
                

def menù():
    while True:
        print("1. Asignar Sueldos")
        print("2. Clasificar Sueldos")
        print("3. Ver Estadisticas")
        print("4. Reporte de sueldos")
        print("5. Salir")

        opc = int(input("ingrese una opciòn: "))
        
        if opc == 1:
            asignar_sueldos()
            
        if opc == 2:
            clasificar_sueldos()    
        
        elif opc == 3:
            ver_estadisticas()
        elif opc == 4:
            reporte_sueldos()    
        
        elif opc == 5:
            print("has salido")
            break
menù()        