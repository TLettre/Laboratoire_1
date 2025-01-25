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

    global solde
    list_card = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]

    while solde > 0:

        print("bienvenue au jeu de Black Jack")
        time.sleep(2)
        if str(input("Voulez-vous continuer? Yes-(y) or No-(n): ")) == "n":
            return


        mise = int(input("Combien voulez-vous miser ?: "))
        if mise > solde or mise <1 :
            print("Vous ne pouvez pas miser plus que votre solde actuel.")
            continue
       
        else:
            card1=random.randint(1,13)
            list_card.remove(card1)
            card2=random.choice(list_card)
            list_card.remove(card2)

            dealer = card1 + card2

            
            pick=random.choice(list_card)
            list_card.remove(pick)
            print(f"\nvous avez piger un {pick}\n")
            while True:

                

                if input("voulez piger, (y)-(n): ") == "y":
                    card=random.choice(list_card)
                    list_card.remove(card)
                    pick = pick + card
                    print(list_card)
                    print(f"\nvous avez piger un {card} pour un total de {pick}\n")

                    if pick > 21:
                        print(dealer)
                        print("GAME LOSE")
                        solde = solde-mise
                        time.sleep(5)
                        return

                else:
                    print()
                    print(dealer)
                    print()
                    if dealer > 21:
                        print ("GAME WIN")
                        solde=solde+mise
                        time.sleep(5)
                        return
                    if dealer > pick:
                        print("GAME LOSE")
                        solde=solde-mise
                        time.sleep(5)
                        return
                    print("GAME WIN")
                    solde=solde+mise
                    time.sleep(5)
                    return



#Menu
while True:

    if solde == 0:
        print("votre solde a atteint 0$\nVeillez suivre les étape suivante pour le remplir a nouveau:\nAppelez au 579-420-3585 et fournissez votre numéro de carte de crédit,votre date d'expiration ainsi que votre CVV")
        print("Le montant choisi sera ajouté à votre balance dans la prochaine heure")
        print()
        time.sleep(10)
        montant=int(input("veuiller choisir le montant souhaité: "))
        print("veuillez patienter\n")
        solde=montant

        time.sleep(30)
        print("votre solde a été actualisé.\nBon jeu")
        time.sleep(3)
        
    print(f"\nvotre solde et de {solde}$\n  ")

    
    choice = str(input("Quelle jeu voulez-avous choisir. (A)-(B)-(C)-(D): "))
    if choice == "D" or choice == "d":
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
    





