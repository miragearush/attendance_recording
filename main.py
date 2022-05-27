from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import os
from chatbot import ChatBot
from developer import Developer
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendace import Attendance
from developer import Developer
from chatbot import ChatBot

# import mysql.connector
class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # first image
        img = Image.open(r"college_images\main_cover_left.png")
        img = img.resize((350, 230), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=350, height=230)
        # second image
        img1 = Image.open(r"college_images\main_cover.png")
        img1 = img1.resize((510, 230), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=350, y=0, width=510, height=230)
        # third image
        img2 = Image.open(r"college_images\main_cover_right.png")
        img2 = img2.resize((400, 230), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=860, y=0, width=400, height=230)
        # background image
        img3 = Image.open(r"college_images\bg.png")
        img3 = img3.resize((1530, 560), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=230, width=1530, height=560)

        # student button
        img4 = Image.open(r"college_images\student_details.png")
        img4 = img4.resize((150, 150), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200, y=10, width=150, height=150)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="brown",fg="white")
        b1_1.place(x=200, y=130, width=150, height=40)

        #detect face button
        img5 = Image.open(r"college_images\face_recog.png")
        img5 = img5.resize((150, 150), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=500, y=10, width=150, height=150)

        b1_1 = Button(bg_img, text="Face Recognition", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"),
                      bg="brown", fg="white")
        b1_1.place(x=500, y=130, width=150, height=40)

        #Attendance button
        img6 = Image.open(r"college_images\attendance.png")
        img6 = img6.resize((150, 150), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b1.place(x=800, y=10, width=150, height=150)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"),
                      bg="brown", fg="white")
        b1_1.place(x=800, y=130, width=150, height=40)

        #train face button
        img7 = Image.open(r"college_images\train_data.png")
        img7 = img7.resize((150, 150), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=200, width=150, height=150)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"),
                      bg="brown", fg="white")
        b1_1.place(x=200, y=330, width=150, height=40)

        # Photos button
        img8 = Image.open(r"college_images\photos.png")
        img8 = img8.resize((150, 150), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=200, width=150, height=150)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"),
                      bg="brown", fg="white")
        b1_1.place(x=500, y=330, width=150, height=40)

        # about Us
        img9 = Image.open(r"college_images\aboutus.png")
        img9 = img9.resize((150, 150), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.developer_data)
        b1.place(x=800, y=200, width=150, height=150)

        b1_1 = Button(bg_img, text="About Us", cursor="hand2",command=self.developer_data ,font=("times new roman", 15, "bold"),
                      bg="brown", fg="white")
        b1_1.place(x=800, y=330, width=150, height=40)

        #helpdesk
        img10 = Image.open(r"college_images\help_desk_icon.jpg")
        img10 = img10.resize((150, 150), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.help_desk)
        b1.place(x=1050, y=10, width=150, height=150)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_desk, font=("times new roman", 15, "bold"),
                      bg="brown", fg="white")
        b1_1.place(x=1050, y=130, width=150, height=40)


        # Exit
        img11 = Image.open(r"college_images\exit.png")
        img11 = img11.resize((150, 150), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.iExit)
        b1.place(x=1050, y=200, width=150, height=150)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"),
                      bg="brown", fg="white")
        b1_1.place(x=1050, y=330, width=150, height=40)

        

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("AMS","Are you sure",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


    #Function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()