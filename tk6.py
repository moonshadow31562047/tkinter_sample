import tkinter as tk

def action_btn_press():
    print("Button was pressed!")

root = tk.Tk()
root.title("部品(widget)の作成")
#アクションの組み込み
root.geometry("350x150")
lb = tk.Label(text="ラベル")
bt = tk.Button(text="ボタン",command=action_btn_press)
lb.pack()
bt.pack()
root.mainloop()