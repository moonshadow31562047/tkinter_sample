import tkinter as tk

def btn_press():
    print("ボタンが押されました")
root = tk.Tk()
root.geometry("150x80")

bt = tk.Button(bitmap="question",command=btn_press)
bt.pack()
root.mainloop()