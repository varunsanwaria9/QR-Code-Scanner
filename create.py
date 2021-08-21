from tkinter import *
import pyqrcode
from pyautogui import alert

def createQR():
    rootCreate = Tk()
    rootCreate.geometry("300x300")
    rootCreate.title("Create QR Code")
    
    def readVal():
        path = "QRCodes/"
        qr = pyqrcode.create(url.get())
        qr.png(path + fName.get() + ".png",scale=6)
        alert("QR Code Generated")

    Label(rootCreate,text="URL:",font="Corier 12").pack(pady=20)
    url = Entry(rootCreate,width=20)
    url.pack(pady=5)
    Label(rootCreate,text="File Name:",font="Corier 12").pack(pady=20)
    fName = Entry(rootCreate,width=20)
    fName.pack(pady=5)
    Button(rootCreate,text="Submit",command=readVal).pack(pady=15)

    rootCreate.mainloop()
