import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
lb = tk.Label(text="This is a LabelThis is a Label,This is a Label")
ms = tk.Message(text="This is a Message,This is a Message,This is a Message")
[widget.pack() for widget in (lb,ms)]

root.mainloop()