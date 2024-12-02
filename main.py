import tkinter as tk
import random
from PIL import Image, ImageTk

#Initialize Window
win = tk.Tk()
win.geometry("900x700")
win.title("Slot Machine")

#Load and Resize Images

def load_image(image_path):
    img = Image.open(image_path)
    img = img.resize((240, 240))
    return ImageTk.PhotoImage(img)

#Initialize Images
ora = load_image("C:/PyCasino/images/orange.jpg")
ban = load_image("C:/PyCasino/images/ban.jpg")
grape = load_image("C:/PyCasino/images/grape.jpg")
base = load_image("C:/PyCasino/images/win.jpg")

money= [300]

label=tk.Label(win,text="Spin To Win!",font=('arial',60))
label.pack()

#Create slot frame
slotframe = tk.Frame(win,bg="red",padx=10,pady=10)
slotframe.columnconfigure(0,weight=1)
slotframe.columnconfigure(1,weight=1)
slotframe.columnconfigure(2,weight=1)

slotframe.pack()

cost= tk.Label(win,text="Spin Cost: $10", font=('arial',20))
cost.pack()

money_label = tk.Label(win, text=f"Money: ${money[0]}", font=('arial', 20))
money_label.pack()


def spin():
    if money[0]-10 <0:
        win_label = tk.Label(win, text="Not enough money! Game Over.", font=('arial', 30))
        win_label.pack()
        win.after(3000, win.destroy)
        return
    
    money[0] -= 10

    money_label.config(text=f"Money: ${money[0]}")
        
    n1 = random.randrange(1,4) 
    n2 = random.randrange(1,4)
    n3 = random.randrange(1,4)

    if n1 == n2 and n2 == n3:
        win_label=tk.Label(win,text="BIG WINNER!",font=('arial',30))
        win_label.pack()
        money[0]+=50
        money_label.config(text=f"Money: ${money[0]}")
        win_label.after(3000,win_label.destroy)
    elif n1 == n2:
        win_label=tk.Label(win,text="WINNER!",font=('arial',30))
        win_label.pack()
        money[0]+=7
        money_label.config(text=f"Money: ${money[0]}")
        win_label.after(3000,win_label.destroy)
        
    s1i = ora if n1 == 1 else ban if n1 == 2 else grape
    s2i = ora if n2 == 1 else ban if n2 == 2 else grape
    s3i = ora if n3 == 1 else ban if n3 == 2 else grape

    for widget in slotframe.winfo_children():
        widget.destroy()

    tk.Label(slotframe,image=s1i).grid(row=1,column=1)
    tk.Label(slotframe,image=s2i).grid(row=1,column=2)
    tk.Label(slotframe,image=s3i).grid(row=1,column=3)

    
tk.Label(slotframe, image=base).grid(row=1, column=1)
tk.Label(slotframe, image=base).grid(row=1, column=2)
tk.Label(slotframe, image=base).grid(row=1, column=3)

spb = tk.Button(win,text="SPIN",bg="red",fg="white",command=spin,width=20,font=('arial',30))
spb.pack(pady=20)




win.mainloop()