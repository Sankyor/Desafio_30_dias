#4. Rock Paper Scissors against the Computer
import random

mano = ("Piedra", "Papel","Tijeras")
computadora = random.randint(0,2)
yo = input("\n\n\n\n\n\n\n Ingrese 1 para Piedra, 2 para Papel, 3 para Tijeras:  ")
print("\n")
ganaste= "Jugador Gana!"
perdiste= "Computadora Gana!"
empataron = "Empataron!"


try:
    yo=int(yo)
    print("La computadora ha seleccionado: ", mano[int(computadora)], " , Y tu has seleccionado: ", mano[yo], "\n")
    if (yo==0 and computadora==1):
        print(perdiste)    
    elif(yo==0 and computadora==2):
        print(ganaste)
    elif(yo==1 and computadora==0):
            print(ganaste)
    elif(yo==1 and computadora==2):
            print(perdiste)
    elif(yo==2 and computadora==0):
            print(perdiste)
    elif(yo==2 and computadora==1):
            print(ganaste)
    else:
        print(empataron)
           
            
except Exception as e:
    print("Ha ocurrido un error en el ingreso")

    
