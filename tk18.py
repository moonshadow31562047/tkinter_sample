import tkinter as tk
def print_txval():
    val_en = en.get()
    print(val_en)

root = tk.Tk()
en = tk.Entry()
bt = tk.Button(text="ボタン",command=print_txval)
[widget.pack() for widget in (en,bt)]

en.focus_set()
root.mainloop()