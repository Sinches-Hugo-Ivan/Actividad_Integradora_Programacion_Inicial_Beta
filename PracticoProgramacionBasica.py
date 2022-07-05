from ast import Try
import os
clear = lambda: os.system('cls')
 #definimos una lista vacia
 
lista=[]

def Pantalla1():
    clear()
    active = False
    while not active:
        
        try:
           #disponemos un ciclo de 5 vueltas
            for x in range(5):
              valor=int(input('Comenzamos a crear una lista de 5 enteros, ingrese de a uno:'))
              lista.append(valor)
       
            #imprimimos la lista    
            print("La Lista es: " ,lista)
            input("Presione ENTER para volver al menu...")
                 
            return menu
        except:
            print('Por favor introduzca un numero entero')
        

                 
             
       

def Pantalla2():
    clear()
    active = False
    while not active:
       # recibe como parámetro la lista y devuelve la suma total de todos sus elementos 
       print("La Suma es: " ,sum(lista))
       input("Presione ENTER para volver al menu...")
       return menu

def Pantalla3():
    clear()
    active = False
    while not active:
        # recibe como parámetro la lista y devuelve el promedio de sus elementos.
        prom = sum(lista) / len(lista)
        print("El Promedio es: " ,prom)
        input("Presione ENTER para volver al menu...")
        return menu

def Pantalla4():
    clear()
    active = False
    while not active:
        #  recibe como parámetro la lista y devuelve el valor máximo de todos los elementos que contiene.
        print("El Maximo es: " ,max(lista))
        input("Presione ENTER para volver al menu...")
        return menu

def Pantalla5():
    clear()
    active = False
    while not active:
      # recibe como parámetro la lista y devuelve el valor mínimo de todos los elementos que contiene.
      print("El Minimo es: " ,min(lista))
      input("Presione ENTER para volver al menu...")
      return menu



menu= active = False
while not active:
    clear()
    print('Actividad Integradora Programacion Inicial:')
    print('1 - Función Lista de enteros: El usuario debe ingresar 5 números enteros, los cuales serán almacenados en una lista.')
    print('2 - Función Suma: recibe como parámetro la lista y devuelve la suma total de todos sus elementos.')
    print('3 - Función Promedio: recibe como parámetro la lista y devuelve el promedio de sus elementos.')
    print('4 - Función Máximo: recibe como parámetro la lista y devuelve el valor máximo de todos los elementos que contiene.')
    print('5 - Función Mínimo: recibe como parámetro la lista y devuelve el valor mínimo de todos los elementos que contiene.')
    print('6 - Exit')
    opcion = input('Introduce un numero:')
    
            
    try:
        if int(opcion) == 1:
            Pantalla1()
        elif int(opcion) == 2:
            Pantalla2()
        elif int(opcion) == 3:
            Pantalla3()
        elif int(opcion) == 4:
            Pantalla4()
        elif int(opcion) == 5:
            Pantalla5()
        elif int(opcion) == 6:
            print(r""" 

            
             11                                                                                          
            100111111111110    0000000    100000000000   00000000000001         10000000001              
                           0   0000000   0000000000000   0000000000000000     0000000000001              
                 101   111 10  0000001  00000000000001   10000001100000000   0000000000000               
                 111  01 1     0000001 1000001           1000001    0000001  0000001                     
        11           11        0000001 1000001           1000001    1000001 1000000                      
        001111 111 11          0000001  00000000011      1000001    1000001 1000000                      
            101       111      0000001   0000000000001   1000001   10000001 1000000                      
            111          0     0000001     110000000001  10000000000000000  1000000                      
                         11    0000001          1000000  1000000000000001   1000000                      
      101  1         1   101   0000001           000000  100000011111       10000001                     
      1011111          11 111  0000001  000000000000001  1000001             00000000111001              
             100               0000001 100000000000000   1000001              0000000000000              
             101     10        0000000 10000000000001    0000000                10000000000              
                       0                                                                                 
                        01                                                                               
                         1111111111111 11  1 1   1 111 1 1 11111 1111111 11111 111 11  1 11 

                           INSTITUTO  SUPERIOR POLITECNICO CORDOBA "INNOVACIÓN CON TECNOLOGIAS 4.0"    
                                 
            DEVELOPERS :   SINCHES HUGO IVAN , GONZALES LEANDRO EMANUEL , TRASMONTANA MARIANO B.  

            " NUNCA DEJES DE APRENDER , NUNCA DEJES DE PROGRAMAR!"
            """)    
            active = True   
    except:
        print("Por favor introduzca una opcion valida")

     
                                                                                                                                                      
                 
    