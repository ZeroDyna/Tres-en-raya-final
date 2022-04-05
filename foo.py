"""
Tres en raya:

Este programa simula el clásico juego tres en  raya,  en
el que dos jugadores marcan alternadamente los  espacios
de un tablero de 3x3 buscando llenar una línea vertical,
horizontal o diagonal con 3 de sus símbolos.

Este programa es parte del desarrollo del curso Programación
de Videojuegos de la carrera Ciencias de la Computación de la 
UCSP.

"""

#Asignación de variables

lista_casilleros = ["_","_","_","_","_","_","_","_","_"]    #Lista de casilleros que se cambiarán por los símbolos de los jugadores según avance el juego.
turno = 0                                                   #Variable turno que irá incrementándose.
signos = ["x","O"]                                          #Signos que se usarán para los dos jugadores.

#Bucle para continuar los turnos

while (turno < 9):                                          #Bucle while que finaliza en el N° máximo de turnos (9).
    turno = turno + 1                                       
    print ("|" + "|".join(lista_casilleros[0:3]) + "|")     #Print de los casilleros del juego.
    print ("|" + "|".join(lista_casilleros[3:6]) + "|")
    print ("|" + "|".join(lista_casilleros[6:9]) + "|")
    seleccion = int(input("ingrese el número del casillero(1-9): "))     #Variable que contendrá la posición de casillero elegida por el jugador.
    lista_casilleros[seleccion-1] = signos[turno%2]         #Dependiendo del turno par o impar, se asignará el signo a cada jugador.

#Print final del resultado del juego

print ("|" + "|".join(lista_casilleros[0:3]) + "|")         
print ("|" + "|".join(lista_casilleros[3:6]) + "|")
print ("|" + "|".join(lista_casilleros[6:9]) + "|")

print("Fin")




