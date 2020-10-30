
from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import ImageTk,Image

class Login:

    def __init__(self,root):
        self.root=root
        self.root.title("Shop Billing Software")

        #geometry (axb)+distance form x +distance from y`
        self.root.geometry("1500x800")

        # resizable = it takes width and hight boolean Value
        self.root.resizable(True,True)

        #======bg image insert and resize ==========
        self.img=Image.open("login.jpg")

        # resize(width,height)
        self.resized=self.img.resize((1800,900))
        self.bg=ImageTk.PhotoImage(self.resized)
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

        #======Login frame==============
        # relief=border styling- SUNKEN,RAISED,GROOVE,RIDGE


        self.Frame_login=Frame(self.root,bd=8,background="white",relief=GROOVE)
        self.Frame_login.place(x=70,y=280,height=350,width=500)
        self.var=IntVar()

        self.login=Label(self.Frame_login,text="Login",font=("Forte",35,"bold"),bg="white",fg="black").place(x=50,y=20)
        self.rad_1=Radiobutton(self.Frame_login,text="As Seller",height=1,width=10,font=("Aparajita",17,"bold"),bg="white",fg="brown",variable=self.var,value=1).place(x=30,y=100)
        self.rad_2=Radiobutton(self.Frame_login,text="As Purchaser",height=1,width=10,font=("Aparajita",17,"bold"),bg="white",fg="brown",variable=self.var,value=2).place(x=170,y=100)

        self.username_value=StringVar()
        self.username=Label(self.Frame_login,text="Username",font=("Comic Sans MS",13,"bold"),bg="white",fg="black").place(x=50,y=140)
        self.user_entry=Entry(self.Frame_login,font=("Aparajita",15,"bold"),bg="lightgrey",textvariable=self.username_value,relief=RIDGE).place(x=50,y=180,width=350,height=35)

        self.user_paasword_value=StringVar()
        self.paasword=Label(self.Frame_login,text="Paasword",font=("Comic Sans MS",13,"bold"),bg="white",fg="black").place(x=50,y=220)
        self.user_paasword=Entry(self.Frame_login,font=("Aparajita",15,"bold"),bg="lightgrey",textvariable=self.user_paasword_value,relief=RIDGE).place(x=50,y=250,width=350,height=35)

        self.forget_paasword=Button(self.Frame_login,text="Forgot Paasword?",bg="white",fg="brown",font=("Arial Nova",10,"bold"),bd=0,command=self.forgotpaasword).place(x=50,y=290)
        self.login_button=Button(self.root,text="Login",bg="white",fg="brown",font=("Arial Black",15),bd=4,command=self.login_function,relief=RAISED,background="lightyellow").place(x=218,y=610,height=38,width=200)


    def login_function(self):
        if self.var.get()==1:
            if (self.username_value.get()=="" or self.user_paasword_value.get()==""):
                messagebox.showerror("Error","All fields are required",parent=self.root)
            elif self.username_value.get()=="Sudeep_seller_1999" and self.user_paasword_value.get()=="Sudeepkr@1999":
                messagebox.showinfo("Welcome","welcome Mr.Sudeep Kumar",parent=self.root)
            else:
                messagebox.showwarning("Warning","Incorrect Username or Paasword",parent=self.root)

        elif self.var.get()==2:
            if self.username_value.get()=="" or self.user_paasword_value.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            elif self.username_value.get()=="Sudeep_purchaser_1999" and self.user_paasword_value.get()=="Sudeepkr@1999":
                messagebox.showinfo("Welcome","welcome Mr.Sudeep Kumar",parent=self.root)
            else:
                messagebox.showwarning("Warning","Incorrect Username or Paasword",parent=self.root)
        else:
            messagebox.showerror("Error","User type not selected")


    def forgotpaasword(self):
        pass
root=Tk()
obj=Login(root)
root.mainloop()
