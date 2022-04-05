# Tres-en-raya-final
## Descripción
Este programa simula el clásico juego tres en  raya,  en
el que dos jugadores marcan alternadamente los  espacios
de un tablero de 3x3 buscando llenar una línea vertical,
horizontal o diagonal con 3 de sus símbolos.

Este programa es parte del desarrollo del curso Programación
de Videojuegos de la carrera Ciencias de la Computación de la 
UCSP.
Por los alumnos:
Alexis Raul Espinoza Villanueva
Renato Oscar Corrales Peña
Guillermo Aaron Kenan Flor Vilca
## Instrucciones de ejecución
1. Para ejecutar el programa el usuario deberá tener instalado python e ingresar:

    ```
    >>> python3 tres-en-raya-permanente1.py
    ```
 2. Al iniciar el programa mostrará el tablero de 3x3 y solicitará a uno de los jugadores que ingrese un número entre 1 y 9.
    
    ```
    Turno Jugador uno

    |_|_|_|
    |_|_|_|
    |_|_|_|

    Jugador uno ingrese el número del casillero (1-9):
   
    ```
 3. Al introducir el número, el programa actualizará el tablero y mostrará el símbolo del jugador de turno en el casillero que escogió y solicitará al siguiente jugador que ingrese otro número. 

    ```
    ingrese el número del casillero(1-9): 1

    Turno Jugador dos
    |O|_|_|
    |_|_|_|
    |_|_|_|

    Jugador dos ingrese el número del casillero(1-9): 

    ```
 4. Se distribuirán los turnos de manera intercalada y el programa finalizará instantaneamente cuando todas las casillas hayan sido ocupadas por los signos de los jugadores. 

    ```
    |O|x|O|
    |x|O|x|
    |O|x|O|

    Fin
    ```
    
