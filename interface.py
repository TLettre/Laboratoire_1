import tkinter as tk
from tkinter import ttk
import time
game = tk.Tk()
game.geometry("200x400")

click = 0
tap   = 1
price1=100
price2=10000

oflineprice1=100
oflineclick=0



while True:


    def update_label():
        global click
        click = click + oflineclick
        texte.config(text=f"click {click}")
        game.after(1000,update_label)


 
    def onclick():
        global tap
        global texte
        global click
        click = click + tap 
        click = int(click)
        texte.config(text=f"click {click}")


    def upgrade1():
        global tap
        global click
        global price1
        global price3
        if click >= price1:
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
            click= int(click)
            tap= int(tap)
            texte.config(text=f"click: {click}")
            taptexte.config(text=f"tap: {tap}")
            button4.config(text=f"{price3} = *1.05")

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
            print(oflineclick)
            if oflineclick == 1:
                update_label()

    
    texte = tk.Label(game, text=(f" click: {click}"))
    texte2 = tk.Label(game, text=("ofline gain"))
    taptexte= tk.Label(game, text=(f"tap: {tap}"))

    button1 = tk.Button(game, text="Cliquez-moi", command = onclick)
    button2 = tk.Button(game, text=f"{price1} = +1", command=upgrade1 )
    button3 = tk.Button(game, text=f"{price2} = +10", command= upgrade2)
    button4 = tk.Button(game, text=" 200 tap needed = *1.02", command=upgrade3)
    oflinebutton1= tk.Button(game, text=f"{oflineprice1} = +1s",command=upgrade4 )


    texte.pack(pady=5)
    taptexte.pack(pady=5)

    button1.pack(pady=5)
    button2.pack(pady=5)
    button3.pack(pady=5)
    button4.pack(pady=5)

    texte2.pack(pady=5)

    oflinebutton1.pack(pady=5)


  
    game.mainloop()

