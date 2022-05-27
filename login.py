
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from matplotlib.pyplot import text
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.bg=ImageTk.PhotoImage(file=r"college_images\bg.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)

        frame=Frame(self.root,bg="#CDC0B0")
        frame.place(x=460,y=170,width=340,height=450)

        get_str=Label(frame,text="Sign in",font=("times new roman",20,"bold"),fg="#8B5742",bg="#CDC0B0") #lightsalmon4 antiquewhite3
        get_str.place(x=130,y=50)

        #label
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="#8B5742",bg="#CDC0B0") #lightsalmon4 antiquewhite3)
        username_lbl.place(x=50,y=130)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=50,y=160,width=250)

        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="#8B5742",bg="#CDC0B0") #lightsalmon4 antiquewhite3)
        password_lbl.place(x=50,y=200)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=50,y=230,width=250)

        #login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="#8B5742",bg="#EEDFCC",activebackground="#EEDFCC")# antiquewhite2
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register button
        registerbtn=Button(frame,text="New User? Sign Up",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,relief=RIDGE,fg="#8B5742",bg="#CDC0B0",activebackground="#CDC0B0")# antiquewhite3
        registerbtn.place(x=20,y=360,width=170)

        #forgot password button
        forgotpassbtn=Button(frame,text="Reset Password",command=self.forgot_pass_window,font=("times new roman",12,"bold"),borderwidth=0,relief=RIDGE,fg="#8B5742",bg="#CDC0B0",activebackground="#CDC0B0")# antiquewhite3
        forgotpassbtn.place(x=15,y=390,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required")
        elif self.txtuser.get()=="arush" and self.txtpass.get()=="arush":
            messagebox.showinfo("Success","Welcome to AMS")
        else:
            conn=mysql.connector.connect(host="localhost",user="ams",password="amspass",database="ams")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or password",parent=self.root2)
            else:
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_System(self.new_window)
            conn.commit()
            conn.close()

    #reset password
    def reset_pass(self):
        if self.combo_securityQ.get=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.securityA_entry.get()=="":
            messagebox.showerror("Error","Enter security Answer",parent=self.root2)
        elif self.newpass.get()=="":
            messagebox.showerror("Error","Enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="ams",password="amspass",database="ams")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_securityQ.get(),self.securityA_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query1=("update register set pass=%s where email=%s")
                value=(self.newpass.get(),self.txtuser.get())
                my_cursor.execute(query1,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password changed successfully",parent=self.root2)
                self.root2.destroy()


    def forgot_pass_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset")
        else:
            conn=mysql.connector.connect(host="localhost",user="ams",password="amspass",database="ams")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Attendance Management System")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="#8B5742")
                l.place(x=0,y=10,relwidth=1)

                securityQ_lbl=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),fg="#8B5742") #lightsalmon4 antiquewhite3)
                securityQ_lbl.place(x=50,y=80)

                self.combo_securityQ=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_securityQ["values"]=("Select","Your Birth Place","Pet Name","Place you like")
                self.combo_securityQ.place(x=50,y=120,width=200)
                self.combo_securityQ.current(0)

                securityA_lbl=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="#8B5742") #lightsalmon4 antiquewhite3)
                securityA_lbl.place(x=50,y=160)

                self.securityA_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.securityA_entry.place(x=50,y=200,width=200)

                newpassword_lbl=Label(self.root2,text="Enter New Password",font=("times new roman",15,"bold"),fg="#8B5742") #lightsalmon4 antiquewhite3)
                newpassword_lbl.place(x=50,y=240)

                self.newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.newpass.place(x=50,y=280,width=200)

                btn=Button(self.root2,text="Reset Password",command=self.reset_pass,font=("times new roman",15,"bold"),fg="#8B5742",bg="#CDC0B0")
                btn.place(x=75,y=340)

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
        b2=Button(frame,command=self.return_login,image=self.photoimg1,borderwidth=0,cursor="hand2")
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

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()