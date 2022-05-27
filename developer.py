from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #top image
        img_top = Image.open(r"college_images\aboutus_cover.png")
        img_top = img_top.resize((1270, 250), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1270, height=250)

        #background image
        img_dev_bg = Image.open(r"college_images\bg.png")
        img_dev_bg = img_dev_bg.resize((1270, 435), Image.ANTIALIAS)
        self.photoimg_dev_bg = ImageTk.PhotoImage(img_dev_bg)

        dev_bg_img = Label(self.root, image=self.photoimg_dev_bg)
        dev_bg_img.place(x=0, y=250, width=1270, height=435)
        
        #frame
        main_frame=Frame(dev_bg_img,bd=2,bg="white")
        main_frame.place(x=50,y=50,width=1150,height=330)

        dev1 = Image.open(r"college_images\dev1.jpg")
        dev1 = dev1.resize((150, 200), Image.ANTIALIAS)
        self.photodev1 = ImageTk.PhotoImage(dev1)

        f_lbl = Label(main_frame, image=self.photodev1)
        f_lbl.place(x=250, y=0, width=150, height=200)

        dev1_1_label=Label(main_frame,text="Arush Kumar",font=("times new roman", 18, "bold"),bg="white",fg="brown")
        dev1_1_label.place(x=250,y=210)

        dev1_2_label=Label(main_frame,text="14017702019",font=("times new roman", 18, "bold"),bg="white",fg="brown")
        dev1_2_label.place(x=250,y=250)
        dev1__3label=Label(main_frame,text="BCA-6C",font=("times new roman", 18, "bold"),bg="white",fg="brown")
        dev1__3label.place(x=250,y=290)

        dev2 = Image.open(r"college_images\dev2.jpg")
        dev2 = dev2.resize((150, 200), Image.ANTIALIAS)
        self.photodev2 = ImageTk.PhotoImage(dev2)

        f_lbl = Label(main_frame, image=self.photodev2)
        f_lbl.place(x=500, y=0, width=150, height=200)

        dev2_1_label=Label(main_frame,text="Ayush Yadav",font=("times new roman", 18, "bold"),bg="white",fg="brown")
        dev2_1_label.place(x=500,y=210)
        dev2_2_label=Label(main_frame,text="13617702019",font=("times new roman", 18, "bold"),bg="white",fg="brown")
        dev2_2_label.place(x=500,y=250)
        dev2__3label=Label(main_frame,text="BCA-6C",font=("times new roman", 18, "bold"),bg="white",fg="brown")
        dev2__3label.place(x=500,y=290)
        

        dev3 = Image.open(r"college_images\dev3.jpeg")
        dev3 = dev3.resize((150, 200), Image.ANTIALIAS)
        self.photodev3 = ImageTk.PhotoImage(dev3)

        f_lbl = Label(main_frame, image=self.photodev3)
        f_lbl.place(x=750, y=0, width=150, height=200)

        dev3_1_label=Label(main_frame,text="Aayush Tiwari",font=("times new roman", 18, "bold"),bg="white",fg="brown")
        dev3_1_label.place(x=750,y=210)
        dev3_2_label=Label(main_frame,text="36617702019",font=("times new roman", 18, "bold"),bg="white",fg="brown")
        dev3_2_label.place(x=750,y=250)
        dev3__3label=Label(main_frame,text="BCA-6C",font=("times new roman", 18, "bold"),bg="white",fg="brown")
        dev3__3label.place(x=750,y=290)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()