import time
import random

solde=100

## Jeu 1: Jeu de hazard suprème

def jeu1(i):
    
    global solde
    print("Bienvenue au jeu de hazard suprème!")
    print(f"Votre solde initial est de {solde}$.\n")


## SYSTEM de mise

    while solde > 0:
        if str(input("Voulez-vous continuer? Yes-(y) or No-(n): ")) == "n":
            return


        mise = int(input("Combien voulez-vous miser ?: "))
        if mise > solde or mise <1 :
            print("Vous ne pouvez pas miser plus que votre solde actuel.")
            continue
       
        else:
                
##end

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
                        time.sleep(2)
                        
                        print(f"Dommage ! Vous avez perdu {mise}$.")
                        print(f"Votre solde actuel est de {solde}$.\n")
                        i=10
                        break
                    time.sleep(0.02)

## Jeu 2: (Jeu de dés)
def jeu2():

    global solde

    print("Bienvenue au jeu de dés!")
    print(f"Votre solde initial est de {solde}$.\n")

    time.sleep(1)

    while solde > 0:
        if str(input("Voulez-vous continuer? Yes-(y) or No-(n): ")) == "n":
            return

        mise = int(input("Combien voulez-vous miser ? "))
        if mise > solde or mise < 1:
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


## Jeu 3 (black jack)

def jeu3():
    dealer = random.randint(1,13)+random.randint(1,13)
    

    pick=random.randint(1,13)
    print(pick)
    print()
    while True:

        if input("voulez piger, (y)-(n): ") == "y":
            pick = pick + random.randint(1,13)
            print(pick)
            print()

            if pick > 21:
                print(dealer)
                print("GAME LOSE")
                time.sleep(5)
                return

        else:
            print()
            print(dealer)
            print()
            if dealer > 21:
                print ("GAME WIN")
                time.sleep(5)
                return
            if dealer > pick:
                print("GAME LOSE")
                time.sleep(5)
                return
            print("GAME WIN")
            time.sleep(5)
            return







#Menu
while True:

    if solde == 0:
        print("votre solde a atteint 0$\nVeillez suivre les étape suivante pour le remplir a nouveau:\nAppelez au 579-420-3585 et fournissez votre numéro de carte de crédit,votre date dexpiration ainsi que votre CVV")
        print("Le montant choisi sera ajouté à votre balance dans la prochaine heure")
        print()
        time.sleep(10)
        montant=int(input("veuiller choisir le montant souhaité: "))
        print("veillez patienter\n")
        solde=montant

        time.sleep(30)
        print("votre solde a été actualisé.\nBon jeu")
        time.sleep(3)
        
    print(f"\nvotre solde et de {solde}$\n  ")

    
    choice = str(input("Quelle jeu voulé vous choisir. (A)-(B)-(C)-(D): "))
    if choice == "D":
        choice = old_choice


    if choice == "a" or choice == "A":
        old_choice = choice
        jeu1(10)

    elif choice == "b" or choice == "B":
        old_choice = choice
        jeu2()
    elif choice == "c" or choice == "C":
        old_choice = choice
        jeu3()
    





