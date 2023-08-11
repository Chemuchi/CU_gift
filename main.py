import tkinter as tk
from bs import *

def on_submit():
    try:
        code = int(entry.get())
        date, location = cu(code)
        result = f"사용일자 : {date}\n사용지점 : {location}"
        label_result.config(text=str(result))
    except IndexError:
        result = "확인된 정보가 없습니다. 코드를 확인해주세요."
        label_result.config(text=str(result))

def no_space(event):
    if event.keysym == "space":
        return "break"

root = tk.Tk()
root.title("Cu 기프티콘 사용확인")
root.minsize(300, 150)
root.resizable(False, False)

label_entry = tk.Label(root, text="기프티콘 코드 입력:")
label_entry.pack()

entry = tk.Entry(root)
entry.bind("<Key>",no_space)
entry.pack()

button_submit = tk.Button(root, text="확인하기", command=on_submit)
button_submit.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
