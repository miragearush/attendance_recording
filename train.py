from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #top image
        img_top = Image.open(r"college_images\train_cover.png")
        img_top = img_top.resize((1270, 250), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1270, height=250)

        #background image
        img_train_bg = Image.open(r"college_images\bg.png")
        img_train_bg = img_train_bg.resize((1270, 435), Image.ANTIALIAS)
        self.photoimg_train_bg = ImageTk.PhotoImage(img_train_bg)

        train_bg_img = Label(self.root, image=self.photoimg_train_bg)
        train_bg_img.place(x=0, y=250, width=1270, height=435)
        #button
        
        b1_1 = Button(train_bg_img, text="Train Data" ,command=self.train_classifier,cursor="hand2",font=("times new roman",25,"bold"),bg="brown",fg="white")
        b1_1.place(x=500, y=215, width=270, height=55)
 
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')#gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        # train the classifier 
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed")
 
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()