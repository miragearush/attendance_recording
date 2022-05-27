from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Management System")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()

        self.bg=ImageTk.PhotoImage(file=r"college_images\bg.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)

        frame=Frame(self.root,bg="#CDC0B0")
        frame.place(x=250,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Register Your Account Here",font=("times new roman",20,"bold"),fg="#8B5742",bg="#CDC0B0") #lightsalmon4 antiquewhite3)
        register_lbl.place(x=250,y=40)
        
        #labels and entry
        #row 1
        fname_lbl=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="#8B5742",bg="#CDC0B0") #lightsalmon4 antiquewhite3)
        fname_lbl.place(x=100,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=100,y=130,width=200)

        lname_lbl=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="#8B5742",bg="#CDC0B0") #lightsalmon4 antiquewhite3)
        lname_lbl.place(x=450,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        lname_entry.place(x=450,y=130,width=200)

        #row 2
        contact_lbl=Label(frame,text="Contact",font=("times new roman",15,"bold"),fg="#8B5742",bg="#CDC0B0") #lightsalmon4 antiquewhite3)
        contact_lbl.place(x=100,y=170)

        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        contact_entry.place(x=100,y=200,width=200)

        email_lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="#8B5742",bg="#CDC0B0") #lightsalmon4 antiquewhite3)
        email_lbl.place(x=450,y=170)

        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        email_entry.place(x=450,y=200,width=200)

        #row 3
        securityQ_lbl=Label(frame,text="Security Question",font=("times new roman",15,"bold"),fg="#8B5742",bg="#CDC0B0") #lightsalmon4 antiquewhite3)
        securityQ_lbl.place(x=100,y=240)

        self.combo_securityQ=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_securityQ["values"]=("Select","Your Birth Place","Pet Name","Place you like")
        self.combo_securityQ.place(x=100,y=270,width=200)
        self.combo_securityQ.current(0)

        securityA_lbl=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="#8B5742",bg="#CDC0B0") #lightsalmon4 antiquewhite3)
        securityA_lbl.place(x=450,y=240)

        securityA_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        securityA_entry.place(x=450,y=270,width=200)

        #row 4
        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="#8B5742",bg="#CDC0B0") #lightsalmon4 antiquewhite3)
        password_lbl.place(x=100,y=310)

        password_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        password_entry.place(x=100,y=340,width=200)

        confm_password_lbl=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="#8B5742",bg="#CDC0B0") #lightsalmon4 antiquewhite3)
        confm_password_lbl.place(x=450,y=310)

        confm_password_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        confm_password_entry.place(x=450,y=340,width=200)
        
        chk_button=Checkbutton(frame,variable=self.var_check,text="I agree to terms & conditions",font=("times new roman",12,"bold"),fg="#8B5742",bg="#CDC0B0",onvalue=1,offvalue=0)
        chk_button.place(x=100,y=400)

        img = Image.open(r"college_images\register.png")
        img = img.resize((100, 50), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=100,y=450,width=100)

        img1 = Image.open(r"college_images\login.jpg")
        img1 = img1.resize((100, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimg1,borderwidth=0,cursor="hand2")
        b2.place(x=400,y=450,width=100)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms & conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="ams",password="amspass",database="ams")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get(),

                                                                                    ))   
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","User Registered Successfully")         


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()