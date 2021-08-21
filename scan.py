from tkinter import *
from tkinter import filedialog,messagebox
import cv2
import webbrowser
import os

import RegexCheck

def readImage():
    rootImg = Tk()
    rootImg.withdraw()
    path = filedialog.askopenfile(parent=rootImg,
            initialdir=os.getcwd(),
            title="Please select a file",
            filetypes=(("PNG Files","*.png"),("JPG Files",".jpg")))
    if path is not None:
        img = cv2.imread(path.name)
        qrCodeDetector = cv2.QRCodeDetector()
        decodedText,points,_ = qrCodeDetector.detectAndDecode(img)
        if decodedText:
            if RegexCheck.isValidURL(decodedText):
                print("QR Code redirecting to {}".format(decodedText))
                webbrowser.open_new(decodedText)
            else:
                print("QR Code value {}".format(decodedText))
                webbrowser.open_new("https://www.google.com/search?q=" + decodedText)
        else:
            messagebox.showinfo("Reading QR Code","No Value Found")
    else:
        messagebox.showinfo("Reading QR Code","Use a valid file")

def readVideo():
    messagebox.showinfo("Reading QR Code","Use q to quit the window.")
    vid = cv2.VideoCapture(0)
  
    while(True):
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        qrCodeDetector = cv2.QRCodeDetector()
        decodedText,points,_ = qrCodeDetector.detectAndDecode(frame)
        if decodedText:
            if RegexCheck.isValidURL(decodedText):
                webbrowser.open_new(decodedText)
            else:
                webbrowser.open_new("https://www.google.com/search?q=" + decodedText)
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    vid.release()
    cv2.destroyAllWindows()

def readQR():
    rootRead = Tk()
    rootRead.geometry("300x200")
    rootRead.title("Reading QR Code")

    Button(rootRead,text="Read Image",font="Corier 14",command=readImage).pack(pady=20)
    Button(rootRead,text="Read Video",font="Corier 14",command=readVideo).pack(pady=20)

    rootRead.mainloop()
