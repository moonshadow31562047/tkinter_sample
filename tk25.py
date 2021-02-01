import tkinter as tk
def get_text():
    print(txt.get("1.5","3.4"))
#小数点の意味は、左が行数で、右が文字数という意味。※start(↑だと、"1.5"のこと)は、右の文字数が1繰り上げられる。
root =tk.Tk()
txt = tk.Text(width=30,height=5)
bt = tk.Button(text="Get Row1 col6 to Row3 Col4",command=get_text)
#「1行目の6文字目から3行目4列目まで」を、取得するという意味。
[w.pack()for w in (txt,bt)]

root.mainloop()
#col=列(縦),row=行(横)