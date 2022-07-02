import cv2
import easygui
import numpy as np
import imageio
import os
import sys

import tkinter as tk
from tkinter import filedialog
from tkinter import *
import matplotlib.pyplot as plt
from tkinter import messagebox

top= tk.Tk()
top.geometry('600x600')
top.title('make yourself a cartoon')
top.configure(background='#C1E90C')
label= Label(top,foreground='#FBD947',background='#055F76',font=('merlin',40))

def upload():
    ImgPath= easygui.fileopenbox()
    cartoonify(ImgPath)

def cartoonify(ImgPath):
    originalImage= cv2.imread(ImgPath)
    originalImage= cv2.cvtColor(originalImage,cv2.COLOR_BGR2RGB)
    
    grayImage= cv2.cvtColor(originalImage,cv2.COLOR_BGR2GRAY)
    
    smoothGray= cv2.medianBlur(grayImage,5)
    
    borderImage= cv2.adaptiveThreshold(smoothGray, 255, 
        cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 25, 9)
    
    colorImage= cv2.bilateralFilter(originalImage,9,300,300)
    
    finalImage= cv2.bitwise_and(colorImage,colorImage,mask=borderImage)
    
    plt.imshow(finalImage,cmap='gray')
    
    save1= Button(top,text='Save Your Cartoon',command=lambda: save(finalImage,ImgPath),padx=30,pady=5)
    save1.configure(background='#B660F4',foreground='#010E33',font=('merlin',20,'bold'))
    save1.pack(side=TOP,pady=50)

def save(finalImage,ImgPath):
    newName= "cartoonifiedimg"
    path1= os.path.dirname(ImgPath)
    extension= os.path.splitext(ImgPath)[1]
    path= os.path.join(path1,newName+extension)
    cv2.imwrite(path,cv2.cvtColor(finalImage,cv2.COLOR_RGB2BGR))
    msg= "Image saved as "+newName+" at "+path
    tk.messagebox.showinfo(title="succesful",message=msg)

upload= Button(top,text='cartoonify',command=upload,padx=10,pady=5)
upload.configure(background='#B660F4',foreground='#010E33',font=('merlin',20,'bold'))
upload.pack(side=TOP,pady=50)

top.mainloop()