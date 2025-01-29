
import tkinter as tk
from tkinter import ttk
import time
game = tk.Tk()
game.geometry("200x400")

click = 0
tap   = 1
price1=100
price2=10000
price3=100000
oflineprice1=100
oflineprice2=1000
oflineclick=0



while True:

    ## loop
    def update_label():
        global click
        click = click + oflineclick
        texte.config(text=f"click: {click}")
        game.after(1000,update_label)


    ## click
    def onclick():
        global tap
        global texte
        global click
        click = click + tap 
        click = int(click)
        texte.config(text=f"click: {click}")

    ## upgrade
    def upgrade1():
        global click
        global price1
        if click >= price1:
            global tap
            global price3
            tap = tap + 1
            click=click-price1
            price1=price1 * 1.1
            price1 = int(price1)
            texte.config(text=f"click: {click}")
            taptexte.config(text=f"tap: {tap}")
            button2.config(text=f"{price1} = +1")
            if tap >= 200:
                price3 = tap * 500
                button4.config(text=f"{price3} = *1.02")
                

    def upgrade2():
        global tap
        global click
        global price2
        global price3
        if click >= price2:
            tap = tap + 10
            click=click-price2
            price2= price2 * 1.1
            price2 = int(price2)
            tap    = int(tap)
            texte.config(text=f"click: {click}")
            taptexte.config(text=f"tap: {tap}")
            button3.config(text=f"{price2} = +10")
            if tap >= 200:
                price3 = tap * 500
                button4.config(text=f"{price3} = *1.02")
                

    def upgrade3():
        global tap
        global click
        global price3
        if click >= price3:
            tap = tap * 1.05
            click=click-price3
            price3=tap*500
            price3= int(price3)
            click= int(click)
            tap= int(tap)
            texte.config(text=f"click: {click}")
            taptexte.config(text=f"tap: {tap}")
            button4.config(text=f"{price3} = *1.05")

    ## Afk upgrade
    def upgrade4():
        global click
        global oflineclick
        global oflineprice1
        if click >= oflineprice1:
            oflineclick=oflineclick+1
            click=click-oflineprice1
            oflineprice1=oflineprice1*1.05
            oflineprice1= int(oflineprice1)
            oflinebutton1.config(text=f"{oflineprice1} = +1s")
            texte.config(text=f"click: {click}")
            afkgain.config(text=f"afk tap: {oflineclick}s")
            if oflineclick == 1:
                update_label()
            if oflineclick == 25:
                oflinebutton2.config(text=f"{oflineprice2} = +10s")


    def upgrade5():
        global click
        global oflineprice2
        global oflineclick
        if oflineclick >= 25:
            if click >= oflineprice2:
                oflineclick=oflineclick + 10
                click=click-oflineprice2
                oflineprice2=oflineprice2*1.05
                oflineprice2=int(oflineprice2)
                oflinebutton2.config(text=f"{oflineprice2} = +10s")
                texte.config(text=f"click: {click}")
                afkgain.config(text=f"afk tap: {oflineclick}s")

            

    ## Interface
    
    texte = tk.Label(game, text=(f" click: {click}"))
    texte2 = tk.Label(game, text=("afk gain"))
    taptexte= tk.Label(game, text=(f"tap: {tap}"))
    afkgain= tk.Label(game, text=(f"afk tap: {oflineclick}s"))
    upgade= tk.Label(game, text=("upgrade"))

    button1 = tk.Button(game, text="Cliquez-moi", command = onclick)
    button2 = tk.Button(game, text=f"{price1} = +1", command=upgrade1 )
    button3 = tk.Button(game, text=f"{price2} = +10", command= upgrade2)
    button4 = tk.Button(game, text=" 200 tap needed = *1.02", command=upgrade3)
    oflinebutton1= tk.Button(game, text=f"{oflineprice1} = +1s",command=upgrade4 )
    oflinebutton2= tk.Button(game, text="25 afk tap needed = +10s",command=upgrade5)
    oflinebutton3= tk.Button(game, text="")
    ## Visual

    texte.pack(pady=5)
    taptexte.pack(pady=5)
    afkgain.pack(pady=5)

    button1.pack(pady=15)

    upgade.pack(pady=5)

    button2.pack(pady=5)
    button3.pack(pady=5)
    button4.pack(pady=5)

    texte2.pack(pady=5)

    oflinebutton1.pack(pady=5)
    oflinebutton2.pack(pady=5)


    
    game.mainloop()

