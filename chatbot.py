from cProfile import label
from tkinter import*
from tkinter import ttk
from turtle import right
from PIL import Image,ImageTk

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("Help Desk")
        self.root.geometry("1530x790+0+0")
        self.root.bind('<Return>',self.enter_func)


        main_frame=Frame(self.root,bd=4,bg='white',width=730)
        main_frame.pack()
        
        img_chat=Image.open(r"college_images\bot_icon.png")
        img_chat=img_chat.resize((250,250),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=1530,compound=LEFT,image=self.photoimg,text='   Ask Me Anything',font=('arial',30,'bold'),fg='white',bg='brown')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=15,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_l=Label(btn_frame,text="Type Here ...",font=('times new roman',14,'bold'),fg='brown')
        label_l.grid(row=0,column=0,padx=5,sticky=W)
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send",command=self.send,font=('times new roman',16,'bold'),width=8,fg='white',bg='brown')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear Fields",command=self.clear,font=('times new roman',14,'bold'),width=9,fg='brown')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)


        self.msg=''
        self.label_ll=Label(btn_frame,text=self.msg,font=('times new roman',14,'bold'),fg='brown')
        self.label_ll.grid(row=1,column=1,padx=5,sticky=W)

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
    
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send='You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_ll.config(text=self.msg,fg='brown')
        else:
            self.msg=''
            self.label_ll.config(text=self.msg,fg='brown')

        if(self.entry.get()=='hello' or self.entry.get()=='hi' or self.entry.get()=='hey'):
            self.text.insert(END,'\n'+'Bot: Hello I am a bot and I am here to answer your queries about the Attendance Management System')
        elif(self.entry.get()=='tell me about student details' or self.entry.get()=='student details' or self.entry.get()=='what is student details'):
            self.text.insert(END,'\n'+'Bot: Student Details is the section where you can add(new),update(existing),delete and view the student information and take photo sample too')
        elif(self.entry.get()=='train data' or self.entry.get()=='tell me about train data' or self.entry.get()=='what is train data'):
            self.text.insert(END,'\n'+'Bot: Train data is a section where you can train the existing images of the student and store the trained data in a xml file')
        elif(self.entry.get()=='face recognition'):
            self.text.insert(END,'\n'+'')
        elif(self.entry.get()=='photos'):
            self.text.insert(END,'\n'+'')
        elif(self.entry.get()=='attendance'):
            self.text.insert(END,'\n'+'')
        elif(self.entry.get()=='about us'):
            self.text.insert(END,'\n'+'')
        elif(self.entry.get()=='help desk'):
            self.text.insert(END,'\n'+'')
        elif(self.entry.get()=='exit'):
            self.text.insert(END,'\n'+'')
        elif(self.entry.get()=='attendance'):
            self.text.insert(END,'\n'+'')
        elif(self.entry.get()=='attendance'):
            self.text.insert(END,'\n'+'')

        else:
            self.text.insert(END,"\n"+"Bot: Sorry I didn't get it.Try something like 'student details','about us', ...")

# self.entry.get()==''

if __name__=='__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()