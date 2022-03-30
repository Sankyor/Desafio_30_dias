#5. High Low Guessing Game
#29-03-2022
import random
guess = 0
numberToFind = random.randint(1,1000)
print("El número que debes encontrar es: ", str(numberToFind))
try:
    while(guess==0):
        playerGuess = input("Guess the number: ")
        playerGuess = int(playerGuess)
        if(numberToFind != playerGuess):
            if(numberToFind > playerGuess):
                print("Higher!")    
            else:
                print("Lower!") 
        else:
            print("You win!")
            guess=1
except Exception as e:
    print("There was an error in: {e}")
    

