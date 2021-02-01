import tkinter as tk
def get_selpoint():
    sel_start = txt.index("sel.first")
    sel_end = txt.index("sel.last")
    cursor_point = txt.index("insert")
    lb["text"] = "start: {} end: {} cursor: {}".format(sel_start,sel_end,cursor_point)

root = tk.Tk()
lb = tk.Label()
txt = tk.Text(width=30,height=5)
bt = tk.Button(text="Selected Area",command=get_selpoint)
[w.pack() for w in(lb,txt,bt)]

root.mainloop()