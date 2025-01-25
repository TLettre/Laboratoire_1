import tkinter as tk
from tkinter import ttk
import time
game = tk.Tk()
game.geometry("200x200")

click = 0
tap   = 1

while True:


    def onclick():
        global tap
        global texte
        global click
        click = click + tap 
        texte.config(text=f"click {click}")

    def upgrade1():
        global tap
        global click
        if click >= 100:
            tap = tap + 1
            click=click-100
            texte.config(text=f"click {click}")

        

    texte = tk.Label(game, text=(f" click {click}"))

    button1 = tk.Button(game, text="Cliquez-moi", command = onclick)
    button2 = tk.Button(game, text="100 = +1", command=upgrade1 )


    texte.pack(pady=10)
    button1.pack(pady=10)
    button2.pack(pady=10)
  
    game.mainloop()