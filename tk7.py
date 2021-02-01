import tkinter as tk

def print_txtval():
    val_en = en.get()
    print(val_en)

root = tk.Tk()
root.title("テキストボックス内容の取得")
root.geometry("350x150")

lb = tk.Label(text="ラベル")
en = tk.Entry()
bt = tk.Button(text="ボタン",command=print_txtval)

[widget.pack() for widget in (lb,en,bt)]

root.mainloop()