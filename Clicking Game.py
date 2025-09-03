import tkinter as tk
number = 0
root = tk.Tk()
root.title("Clicking Game")
root.geometry("1366x768")

label = tk.Label(root,font=("Minecraft",32))
label.pack()

btn = tk.Button(root,text="Click Me",font=("Minecraft",32),command=lambda:click())
btn.place(relx=0.5,rely=0.5,anchor='center')

def start():
    global number
    label.config(text=str(number))

def click():
    global number
    number += 1
    label.config(text=str(number))


def Restart():
    global number
    number = 0
    label.config(text=str(number))

def Exit():
    root.quit()

def about():
    ab = tk.Toplevel(root)
    ab.title("About")
    ab.geometry("341x192")
    abou = tk.Label(ab,text="Clicking Game Prototype (Build 1) , Made In Python")
    abou.pack()
    ab.mainloop()

def Keybind(event): 
    if event.keysym == "Return":
        global number
        number += 1
        label.config(text=str(number))
    elif event.keysym == "space":
        number += 1
        label.config(text=str(number))
    elif event.keysym == "Escape":
        root.quit()
    elif event.keysym == "r":
        number = 0
        label.config(text=str(number))
    elif event.keysym == "R":
        number = 0
        label.config(text=str(number))

menubar = tk.Menu(root)


file = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Game",menu=file)
file.add_command(label="Restart (R)",command=Restart)
file.add_separator()
file.add_command(label="Exit(Esc)",command=Exit)

Help = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=Help)
Help.add_command(label="About",command=about)

root.config(menu=menubar)

root.bind('<Return>',Keybind)
root.bind('<space>',Keybind)
root.bind('<Escape>', Keybind)
root.bind('<r>', Keybind)
root.bind('<R>', Keybind)

start()
root.mainloop()
