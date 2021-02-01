import tkinter as tk

def return_press(event):
    en_val = strvar.get()
    print(en_val)
    strvar.set("")
    msvar.set(en_val+en_val)

root = tk.Tk()
strvar = tk.StringVar()
en = tk.Entry(textvariable=strvar)
en.bind("<Return>", return_press)
en.pack()
msvar =tk.StringVar()
ms = tk.Message(textvariable=msvar)
ms.pack()

root.mainloop()