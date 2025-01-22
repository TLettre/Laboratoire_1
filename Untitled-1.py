
import time  
import random    
i=10
solde=1000000

while True:

    ############: Menu

    print( )
    print("À quelle jeux voulez-vous jouer.")
    print( )
    time.sleep(1)

    jeu = (input("(a)pour le jeu de hazard suprème, (b) pour le jeu de dés: "))
    print( )
    time.sleep(1)

    #############: Jeu 1

    if jeu == "a":

        print("Bienvenue au jeu de hazard suprème!")
        print(f"Votre solde initial est de {solde}$.\n")

        while solde > 0:

            mise = int(input("Combien voulez-vous miser ? "))
            if mise > solde:
                print("Vous ne pouvez pas miser plus que votre solde actuel.")
                continue
            
            else:
            
                while True:

                    x= random.randint(1, 2)
                    if x == 1:
                        i=i+1
                        print(i)

                    else:
                        i=i-1
                        print(i)

                    if i == 20:
                        print("GAME WIN")
                        solde=solde + mise
                        
                        print(f"Félicitations ! Vous avez gagné {mise}$.")
                        print( )
                        time.sleep(2)
                        print(f"Votre solde actuel est de {solde}$.\n")
                        i=10
                        break
                        
                    if i == 0:
                        print("GAME LOSE")
                        solde= solde - mise
                        
                        print(f"Dommage ! Vous avez perdu {mise}$.")
                        print( )
                        time.sleep(2)

                        print(f"Votre solde actuel est de {solde}$.\n")
                        i=10
                        break



                    time.sleep(0.02)


    #############: Jeu 2

    if jeu == "b":

        print("Bienvenue au jeu de dés!")
        print(f"Votre solde initial est de {solde}$.\n")

        time.sleep(1)

        while solde > 0:

            mise = int(input("Combien voulez-vous miser ? "))
            if mise > solde:
                print("Vous ne pouvez pas miser plus que votre solde actuel.")
                continue

            else:


                WinningNumber= random.randint(1, 6)


                if int(input("Choissez un chiffre de 1 à 6: ")) == WinningNumber:

                    print( )
                    print("GAME WIN")
                    print(f"Félicitations ! Vous avez gagné {mise * 5}$.")
                    print( )
                    time.sleep(2)
                    
                    solde= solde + mise*5

                    print(f"Votre solde actuel est de {solde}$.\n")
                    
                else:

                    print( )
                    print("GAME LOSE")
                    print(f"La bonne réponse était {WinningNumber}")
                    print( )
                    time.sleep(1)
                    solde = solde-mise

                    print(f"Dommage ! Vous avez perdu {mise}$.")
                    print(f"Votre solde actuel est de {solde}$.\n")
                    time.sleep(2)
        
    if input() == "oui":
        continue
    elif input() == "non":
        break


