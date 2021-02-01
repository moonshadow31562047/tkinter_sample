import tkinter as tk

root = tk.Tk()
root.geometry("250x250")
ms_dict = {}

for relief_val in ["flat","raised","sunken","groove","ridge"]:

    ms_dict[relief_val] = tk.Message(text=relief_val,relief=relief_val,bd=10)
    ms_dict[relief_val].pack()
# 上の2行は、インデントをつけてから始めないと、「エラー」になる。

root.mainloop()
