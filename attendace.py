from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        #cover image
        img = Image.open(r"college_images\attendance_cover.png")
        img = img.resize((1270, 230), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1270, height=230)

        # background image
        img3 = Image.open(r"college_images\black.jpg")
        img3 = img3.resize((1270, 560), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=230, width=1270, height=560)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=5,width=1255,height=450)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Information",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=5,width=625,height=440)


        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=10,width=610,height=305)

        #labels and entries

        #attendance id

        attendanceId_label = Label(left_inside_frame, text="Attendance ID", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10,pady=5, sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll

        rollLabel = Label(left_inside_frame, text="Roll", font=("times new roman", 12, "bold"), bg="white")
        rollLabel.grid(row=0, column=2, padx=4,pady=8, sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman", 12, "bold"))
        atten_roll.grid(row=0,column=3,pady=8,sticky=W)

        #Name

        nameLabel_label = Label(left_inside_frame, text="Name", font=("times new roman", 12, "bold"), bg="white")
        nameLabel_label.grid(row=1, column=0, padx=10,pady=5, sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman", 12, "bold"))
        atten_name.grid(row=1,column=1,pady=8,sticky=W)

        #Deptartment

        depLabel = Label(left_inside_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        depLabel.grid(row=1, column=2, sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman", 12, "bold"))
        atten_dep.grid(row=1,column=3,pady=8,sticky=W)

        #time

        timeLabel = Label(left_inside_frame, text="Time", font=("times new roman", 12, "bold"), bg="white")
        timeLabel.grid(row=2, column=0, sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman", 12, "bold"))
        atten_time.grid(row=2,column=1,pady=8,sticky=W)

        #date

        dateLabel = Label(left_inside_frame, text="Date", font=("times new roman", 12, "bold"), bg="white")
        dateLabel.grid(row=2, column=2, sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman", 12, "bold"))
        atten_date.grid(row=2,column=3,pady=8,sticky=W)

        #attendance
        attendanceLabel = Label(left_inside_frame, text="Attendance", font=("times new roman", 12, "bold"), bg="white")
        attendanceLabel.grid(row=3, column=0, sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=230,width=600,height=32)

        save_btn=Button(btn_frame,text="Import Attendance",command=self.importCSV,width=32,font=("times new roman", 12, "bold"),bg="brown",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Export Attendance to any format",command=self.exportCSV, width=32, font=("times new roman", 12, "bold"), bg="brown",
                          fg="white")
        update_btn.grid(row=0, column=1)

        reset_btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        reset_btn_frame.place(x=5,y=270,width=630,height=32)

        reset_btn = Button(reset_btn_frame, text="Reset",command=self.reset_data, width=65, font=("times new roman", 12, "bold"), bg="brown",
                          fg="white")
        reset_btn.grid(row=0, column=0)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance ",
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=635, y=5, width=610, height=440)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=600,height=405)

        #scroll bar and table

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
    #fetch data
    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
    #export csv
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data to export",parent=self.root)
                return False

            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data Exported to "+os.path.basename(fln)+" Successfully")
        except Exception as es: 
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()