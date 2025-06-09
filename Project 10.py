import time as t
import threading
import tkinter as tk
power = 1
score = 0
cps = 0

def ADD(): 
    global cps
    global score
    while True: 
        score = score + cps 
        Label.config(text=str(score))
        t.sleep(1)


def click():
    global score
    score = score + power
    Label.config(text=str(score))

def QUIT():
    root.quit()
    quit()

def Restart():
    global score
    score = 0
    Label.config(text=str(score))

def power1():
    global score
    if score >= 25:
        score = score - 25
        Label.config(text=str(score))
        global power
        power = power + 1
    else:
        print("not enough points")

def power5():
    global score
    if score >= 100:
        score = score - 100
        Label.config(text=str(score))
        global power
        power = power + 5
    else:
        print("Not Enough points")

def cps5():
    global score
    global cps
    if score >= 230:
        score = score - 230
        Label.config(text=str(score))
        cps = cps + 5
    else:
        print("Not Enough points")

def power15():
    global score
    if score >= 500:
        score = score - 500
        Label.config(text=str(score))
        global power
        power = power + 20
    else:
        print("Not Enough points")

root = tk.Tk()
Label = tk.Label(root,text="0",font=("Minecraft",32))
Label.pack()
root.geometry("690x420")
root.title("Clicking Game")
button = tk.Button(root,text="Click",font=("Minecraft",32),command=lambda:click())
button.place(relx=0.5,rely=0.5,anchor='center')
menubar = tk.Menu(root,tearoff=0)
game = tk.Menu(menubar,tearoff=0)
game.add_command(label="Restart",command=Restart)
game.add_separator()
game.add_command(label="Exit",command=QUIT)
menubar.add_cascade(label="Game",menu=game)
Upgrades = tk.Menu(menubar,tearoff=0)
Upgrades.add_command(label="+1 Click Power (25 points)",command=power1)
Upgrades.add_command(label="+5 Click Power (100 points)",command=power5)
Upgrades.add_command(label="+15 Click Power (500 points)",command=power15)
Upgrades.add_separator()
Upgrades.add_command(label="+5 Cps (230 points)",command=cps5)
menubar.add_cascade(label="Upgrades",menu=Upgrades)
root.config(menu=menubar)

add = threading.Thread(target=ADD)
add.daemon = True
add.start()

root.mainloop()

print("Program End")