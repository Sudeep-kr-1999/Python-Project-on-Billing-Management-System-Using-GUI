from tkinter import *
from tkinter import Frame
from PIL import Image,ImageTk


class ForgotPaasword:
    def __init__(self,root):
        self.root_1=root
        self.bgcolor = "#074463"
        self.bgcolor6 = "#074463"
        self.bgcolor1 = "grey"
        self.bgcolor2 = "#ECF0F1"
        self.bgcolor3 = "#A1F9F8"
        self.bgcolor4 = "white"
        self.bgcolor5 = "#A4F5F4"

        self.root_1.geometry("500x350+500+280")
        self.root_1.resizable(False,False)
        self.root_1.title("Forgot Paasword Window")
        self.background=Label(self.root_1,bg=self.bgcolor1,bd=15,height=350,width=500,relief=GROOVE).place(x=0,y=0,relheight=1,relwidth=1)
        self.forgot_frame=Frame(self.root_1,bd=10,background="white",relief=RIDGE,bg="lightgrey").place(x=40,y=45,height=250,width=420)
        self.heading=Label(self.root_1,text="Forgot Paasword",font=("Forte",20,"bold"),bg="lightgrey",fg="brown").place(x=60,y=60)

        self.user_name_new=StringVar()
        self.ask_user_id=Label(self.root_1,text="Enter Username",font=("Comic Sans MS",13,"bold"),bg="lightgrey",fg="black").place(x=60,y=90)
        self.user_new_entry=Entry(self.root_1,font=("Aparajita",12,"bold"),bg="white",textvariable=self.user_name_new,relief=RIDGE).place(x=60,y=120,width=280,height=25)

        self.user_new_paasword=StringVar()
        self.ask_new_paasword=Label(self.root_1,text="Enter new Paasword",font=("Comic Sans MS",13,"bold"),bg="lightgrey",fg="black").place(x=60,y=150)
        self.user_new_entry_1=Entry(self.root_1,font=("Aparajita",12,"bold"),bg="white",textvariable=self.user_new_paasword,relief=RIDGE).place(x=60,y=180,width=280,height=25)

        self.user_confirm_new_paasword=StringVar()
        self.confirm_new_paasword=Label(self.root_1,text="Confirm new Paasword",font=("Comic Sans MS",13,"bold"),bg="lightgrey",fg="black").place(x=60,y=210)
        self.user_new_entry_2=Entry(self.root_1,font=("Aparajita",12,"bold"),bg="white",textvariable=self.user_confirm_new_paasword,relief=RIDGE).place(x=60,y=240,width=280,height=25)

        self.submit_button=Button(self.root_1,text="Save",fg="black",font=("Aparajita",14,"bold"),bd=4,relief=RAISED,background="lightyellow").place(x=364,y=150,height=35,width=80)
        self.cancel_button=Button(self.root_1,text="Cancel",fg="black",font=("Aparajita",14,"bold"),bd=4,relief=RAISED,background="lightyellow").place(x=364,y=200,height=35,width=80)

root=Tk()
obj=ForgotPaasword(root)
root.mainloop()

