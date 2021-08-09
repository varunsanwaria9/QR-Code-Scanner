from tkinter import *

import create
import scan

root = Tk()
root.geometry("300x200")
root.title("QR Code")

Button(root,text="Create QR",font="Corier 14",command=create.createQR).pack(pady=20)
Button(root,text="Read QR",font="Corier 14",command=scan.readQR).pack(pady=20)

root.mainloop()