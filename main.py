try:
    import tkinter as tk
    from tkinter.constants import DISABLED, END, FALSE, LEFT, NORMAL, RIGHT
    import csv
    import pandas as pd
    import random
    import string
    from datetime import date
    from tkinter import messagebox
except:
    pass


class Main(tk.Frame):
    

    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.main_configure_gui()
        self.main_widgets()    

    def main_configure_gui(self):
        self.master.title('Login')
        x = self.master.winfo_screenwidth() // 2 - 960 // 2
        y = self.master.winfo_screenheight() // 2 - 540 // 2
        self.master.geometry('960x540+%d+%d' % (x,y))
        self.master.resizable(FALSE,FALSE)
        self.Font_tuple = ('Open Sans', 9, 'bold')
        
    def main_widgets(self):

        Frame_main = tk.Frame(self.master)
        Frame_main.pack(fill="both", expand=True)

        self.background_Image = tk.PhotoImage(file='Images\Background.png')
        tk.Label(Frame_main, 
                image=self.background_Image).place(x=0, y=0, relwidth=1, relheight=1)

        Login_Frame = tk.Frame(Frame_main, bg='#ffffff')
        Login_Frame.place(x=80, y=75, width=300, height=390)

        Login_here = tk.Label(Login_Frame,
                        text='Login Here',
                        font=('Montserrat', 30, "bold"),
                        bg='#ffffff').place(x=35, y=50)
            
        Email_address = tk.Label(Login_Frame,
                        text='Email address:',
                        font = self.Font_tuple,
                        bg='#ffffff').place(x=56, y=150)
        Password = tk.Label(Login_Frame,
                        text='Password:',
                        font = self.Font_tuple,
                        bg='#ffffff').place(x=56, y=190)
        Forgot_password = tk.Label(Login_Frame,
                        text='Forgot Password?',
                        font = self.Font_tuple,
                        bg='#ffffff').place(x=90, y=240)

        self.Email = tk.StringVar()
        self.password = tk.StringVar()
        
        Email_entry = tk.Entry(Login_Frame,
                            bg='lightgrey',
                            textvariable=self.Email,
                            borderwidth=0, width=30).place(x=60, y=170)
        Password_entry = tk.Entry(Login_Frame,
                            bg='lightgrey',
                            textvariable=self.password,
                            borderwidth=0, width=30, show='*').place(x=60, y=210)

        P2 = Logic(self.master,None,None,None,self.Email,self.password,None)

        Login_Button = tk.Button(Login_Frame,
                                text='Login',
                                width=25, borderwidth=0,
                                font = self.Font_tuple,
                                bg='#2d7aee', fg='#ffffff',
                                command=P2.search_user).place(x=60, y=270)
        Register_Bhutton = tk.Button(Login_Frame,
                                text='Create New Account',
                                width=25, borderwidth=0,
                                font = self.Font_tuple,
                                bg='#2d7aee', fg='#ffffff',
                                command=self.register_widgets).place(x=60, y=300)

    def register_widgets(self):

        self.reg_screen = tk.Toplevel(self.master)
        self.reg_screen.title("Sign Up")
        x = self.reg_screen.winfo_screenwidth() // 2 - 320 // 2
        y = self.reg_screen.winfo_screenheight() // 2 - 480 // 2
        self.reg_screen.geometry('320x480+%d+%d' % (x,y))
        self.reg_screen.resizable(FALSE,FALSE)
        
        Frame_reg = tk.Frame(self.reg_screen, bg='#f3f5f6')
        Frame_reg.place(x=0, y=0, width=320, height=480)

        Sign_up = tk.Label(Frame_reg,
                        text='Sign Up',
                        font=('Sans serif', 25, "bold"),
                        bg='#f3f5f6').place(x=95, y=50) 
            
        First_name = tk.Label(Frame_reg,
                        text='First name:',
                        font = self.Font_tuple,
                        bg='#f3f5f6').place(x=66, y=150)
        Last_name = tk.Label(Frame_reg,
                        text='Last name:',
                        font = self.Font_tuple,
                        bg='#f3f5f6').place(x=66, y=190)
        Email_address = tk.Label(Frame_reg,
                        text='Email address:',
                        font = self.Font_tuple,
                        bg='#f3f5f6').place(x=66, y=230)
        Password = tk.Label(Frame_reg,
                        text='Password:',
                        font = self.Font_tuple,
                        bg='#f3f5f6').place(x=66, y=270)

        self.First_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.E_mail = tk.StringVar()
        self.password = tk.StringVar()

        First_name = tk.Entry(Frame_reg,
                            bg='lightgrey',
                            textvariable=self.First_name,
                            borderwidth=0, width=30).place(x=70, y=170)
        Last_name = tk.Entry(Frame_reg,
                            bg='lightgrey',
                            textvariable=self.last_name,
                            borderwidth=0, width=30).place(x=70, y=210)
        E_mail = tk.Entry(Frame_reg,
                            bg='lightgrey',
                            textvariable=self.E_mail,
                            borderwidth=0, width=30).place(x=70, y=250)      
        password_entry = tk.Entry(Frame_reg,
                            bg='lightgrey',
                            textvariable=self.password,
                            borderwidth=0,show='*', width=30).place(x=70, y=290)

        P1 = Logic(self.master,self.reg_screen, self.First_name, self.last_name, self.E_mail, self.password ,None)

        sign_up = tk.Button(Frame_reg,
                            text='Sign Up',
                            width=25, font = self.Font_tuple,
                            borderwidth=0, bg='#2d7aee',
                            fg='#ffffff', command=P1.register_user).place(x=70, y=320)

class Logic:

    def __init__(self,master, reg_screen, Fname, Lname, Email, password, pro_ID):
        self.master = master
        self.reg_screen = reg_screen
        self.First_name = Fname
        self.Last_name = Lname
        self.E_mail = Email
        self.password = password
        self.Product_ID = pro_ID

    def register_user(self):
        User_data = []
        User_data.append(self.First_name.get())
        User_data.append(self.Last_name.get())
        User_data.append(self.E_mail.get())
        User_data.append(self.password.get())
        with open('User_records.txt', "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerows([User_data])
        f.close()
        tk.Label(self.reg_screen,
                text='Sign Up Successfully',
                fg="#007500", font=("calibri", 11),
                bg='#f3f5f6').place(x=95, y=350)
        
    def search_user(self):
        User_ID = self.E_mail.get()
        User_Pass = self.password.get()
        with open("User_records.txt", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if User_ID == row[2]:
                    if User_Pass == row[3]:
                        self.master.destroy()
                        Manage_Frame()
                    else:
                        self.password_not_recognised()

    def password_not_recognised(self):
        tk.Label(self.master,
                text='The email/password you entered is incorrect',
                fg='red', bg='white').place(x=110, y=410)

    def search_product(self):
        Product_ID = self.Product_ID.get()
        with open('Product_records.txt', mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    if Product_ID == row[0]:
                        Home = tk.Tk()
                        Home.title(row[1])
                        x = Home.winfo_screenwidth() // 2 - 960 // 2
                        y = Home.winfo_screenheight() // 2 - 540 // 2
                        Home.geometry('960x540+%d+%d' % (x,y))
                        Home.configure(bg='white')
                        Home.resizable(FALSE,FALSE)
                        tk.Label(Home,text="Coming soon").place(relheight=1,relwidth=1)
                        Home.mainloop()
                except:
                    pass


class Manage_Frame:
     
    def __init__(self):
        self.root = tk.Tk()
        self.configure_gui()

    def configure_gui(self):
        self.root.title('Shopping Cart')
        x = self.root.winfo_screenwidth() // 2 - 960 // 2
        y = self.root.winfo_screenheight() // 2 - 540 // 2
        self.root.geometry('960x540+%d+%d' % (x,y))
        self.root.resizable(FALSE,FALSE)
        container = tk.Frame(self.root)
        container.pack(side = "top", fill = "both", expand = True)
            
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
            
        self.frames = {}
        for F in (Frame_1,Frame_2):
            
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Frame_1)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Frame_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.main_widgets()
        self.Font_tuple = ('Open Sans', 9, 'bold')

    def main_widgets(self):

        main_frame = tk.Frame(self, bg='#f3f5f6')
        main_frame.place(x=0, y=0, width=960, height=540)
        
        Header = tk.Frame(main_frame, bg='#3a3b42')
        Header.place(x=0, y=0, width=960, height=60)

        self.Product_ID = tk.StringVar()

        C2 = Logic(None,None,None,None,None,None,self.Product_ID)
        
        Search_Entry = tk.Entry(Header,width=50, textvariable=self.Product_ID)
        Search_Entry.place(x=85, y=15, height=30)
        self.Search_icon = tk.PhotoImage(file='Images\search.png')
        button = tk.Button(Header,
                        image=self.Search_icon,
                        borderwidth=0, bg='#2d7aee',
                        width=40, command=C2.search_product).place(x=385, y=15, height=30)

        C1 = Cart()

        self.Cart_icon = tk.PhotoImage(file='Images\cart.png')
        button = tk.Button(Header,
                        image=self.Cart_icon,
                        borderwidth=0, bg='#3a3b42',
                        command=C1.configure_gui).place(x=870, y=15, height=30)


        Search_Entry.insert(0, "Search Here")
        Search_Entry.configure(state=DISABLED)
        
        def on_click(event):
            Search_Entry.configure(state=NORMAL)
            Search_Entry.delete(0, END)
            
            Search_Entry.unbind('<Button-1>', on_click_id)
            
        on_click_id = Search_Entry.bind('<Button-1>', on_click)

        Banner = tk.Frame(main_frame)
        Banner.place(x=0, y=90, width=960, height=150)

        self.Banner_Image = tk.PhotoImage(file='Images\Main.png')
        tk.Label(Banner, image=self.Banner_Image).place(x=0, y=0)

        Header_2 = tk.Frame(main_frame, bg='#3a3b42')
        Header_2.place(x=0, y=275, width=960, height=200)
 
        self.Next_icon = tk.PhotoImage(file=r'Images\Next.png')
        tk.Button(main_frame,
                text='Next page',
                image=self.Next_icon,
                compound=RIGHT, borderwidth=0,
                bg='#f3f5f6', fg='#2d7aee',
                command = lambda : self.controller.show_frame(Frame_2)).place(x=820, y=480, height=30)

 
        self.Image_1 = tk.PhotoImage(file='Images\Iphone_12.png')
        tk.Label(main_frame, image=self.Image_1, borderwidth=0).place(x=85, y=300)
        P1 = Product('El-190')
        tk.Button(main_frame,text='add',
                borderwidth=0, bg='#2d7aee',
                fg='#ffffff',width=5,
                command=P1.Add_Item).place(x=194, y=450)
        tk.Button(main_frame,text='remove',
                borderwidth=0,bg='#2d7aee',
                fg='#ffffff',
                command=P1.remove_Item).place(x=85, y=450)

        self.Image_2 = tk.PhotoImage(file='Images\IPad_Pro.png')
        tk.Label(main_frame, image=self.Image_2, borderwidth=0).place(x=245, y=300)
        P2 = Product('El-192')
        tk.Button(main_frame,text='add',
                borderwidth=0, bg='#2d7aee',
                fg='#ffffff',width=5,
                command=P2.Add_Item).place(x=354, y=450)
        tk.Button(main_frame,text='remove',
                borderwidth=0,bg='#2d7aee',
                fg='#ffffff',
                command=P2.remove_Item).place(x=245, y=450)

        self.Image_3 = tk.PhotoImage(file='Images\Airpod_pro.png')
        tk.Label(main_frame, image=self.Image_3, borderwidth=0).place(x=405, y=300)
        P3 = Product('El-193')
        tk.Button(main_frame,text='add',
                borderwidth=0, bg='#2d7aee',
                fg='#ffffff',width=5,
                command=P3.Add_Item).place(x=514, y=450)
        tk.Button(main_frame,text='remove',
                borderwidth=0,bg='#2d7aee',
                fg='#ffffff',
                command=P3.remove_Item).place(x=405, y=450)

        self.Image_4 = tk.PhotoImage(file='Images\Apple_watch.png')
        tk.Label(main_frame, image=self.Image_4, borderwidth=0).place(x=565, y=300)
        P4 = Product('El-194')
        tk.Button(main_frame,text='add',
                borderwidth=0, bg='#2d7aee',
                fg='#ffffff',width=5,
                command=P4.Add_Item).place(x=674, y=450)
        tk.Button(main_frame,text='remove',
                borderwidth=0,bg='#2d7aee',
                fg='#ffffff',
                command=P4.remove_Item).place(x=565, y=450)

        self.Image_5 = tk.PhotoImage(file='Images\Mac_book.png')
        tk.Label(main_frame, image=self.Image_5, borderwidth=0).place(x=725, y=300)
        P5 = Product('El-191')
        tk.Button(main_frame,text='add',
                borderwidth=0, bg='#2d7aee',
                fg='#ffffff',width=5,
                command=P5.Add_Item).place(x=834, y=450)
        tk.Button(main_frame,text='remove',
                borderwidth=0,bg='#2d7aee',
                fg='#ffffff',
                command=P5.remove_Item).place(x=725, y=450)

class Frame_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.Font_tuple = ('Open Sans', 9, 'bold')
        self.controller = controller
        self.main_widgets()

    def main_widgets(self):

        main_frame = tk.Frame(self, bg='#f3f5f6')
        main_frame.place(x=0, y=0, width=960, height=540)
        
        Header = tk.Frame(main_frame, bg='#3a3b42')
        Header.place(x=0, y=0, width=960, height=60)

        self.Product_ID = tk.StringVar()

        C2 = Logic(None,None,None,None,None,None,self.Product_ID)
        
        Search_Entry = tk.Entry(Header, width=50, textvariable=self.Product_ID)
        Search_Entry.place(x=85, y=15, height=30)
        self.Search_icon = tk.PhotoImage(file='Images\search.png')
        button = tk.Button(Header,
                        image=self.Search_icon,
                        borderwidth=0, bg='#2d7aee',
                        width=40, command=C2.search_product).place(x=385, y=15, height=30)

        C1 = Cart()

        self.Cart_icon = tk.PhotoImage(file='Images\cart.png')
        button = tk.Button(Header,
                        image=self.Cart_icon,
                        borderwidth=0, bg='#3a3b42',
                        command=C1.configure_gui).place(x=870, y=15, height=30)

        Search_Entry.insert(0, "Search Here")
        Search_Entry.configure(state=DISABLED)
        
        def on_click(event):
            Search_Entry.configure(state=NORMAL)
            Search_Entry.delete(0, END)
            
            Search_Entry.unbind('<Button-1>', on_click_id)
            
        on_click_id = Search_Entry.bind('<Button-1>', on_click)

        Banner = tk.Frame(main_frame)
        Banner.place(x=0, y=90, width=960, height=150)

        self.Banner_Image = tk.PhotoImage(file='Images\Banner_2.png')
        tk.Label(Banner, image=self.Banner_Image).place(x=0, y=0)

        Header_2 = tk.Frame(main_frame, bg='#3a3b42')
        Header_2.place(x=0, y=275, width=960, height=200)

        self.Next_icon = tk.PhotoImage(file=r'Images\Next.png')
        tk.Button(main_frame,
                text='Next page',
                image=self.Next_icon, compound=RIGHT,
                borderwidth=0, bg='#f3f5f6',
                fg='#2d7aee', font=self.Font_tuple).place(x=820, y=480, height=30)

        self.Back_icon = tk.PhotoImage(file=r'Images\Back.png')
        tk.Button(main_frame,
                text='Back page',
                image=self.Back_icon,
                compound=LEFT, borderwidth=0,
                bg='#f3f5f6', fg='#2d7aee',
                command = lambda : self.controller.show_frame(Frame_1)).place(x=85, y=480, height=30)

        self.Image_1 = tk.PhotoImage(file="Images\Blue_shoe.png")
        button1 = tk.Label(main_frame, image=self.Image_1, borderwidth=1).place(x=85, y=300)
        P1 = Product('Cl-190')
        tk.Button(main_frame,text='add',
                borderwidth=0, bg='#2d7aee',
                fg='#ffffff',width=5,
                command=P1.Add_Item).place(x=195, y=450)
        tk.Button(main_frame,text='remove',
                borderwidth=0,bg='#2d7aee',
                fg='#ffffff',
                command=P1.remove_Item).place(x=85, y=450)


        self.Image_2 = tk.PhotoImage(file='Images\watch.png')
        button = tk.Label(main_frame, image=self.Image_2, borderwidth=0).place(x=245, y=300)
        P2 = Product('Cl-191')
        tk.Button(main_frame,text='add',
                borderwidth=0, bg='#2d7aee',
                fg='#ffffff',width=5,
                command=P2.Add_Item).place(x=354, y=450)
        tk.Button(main_frame,text='remove',
                borderwidth=0,bg='#2d7aee',
                fg='#ffffff',
                command=P2.remove_Item).place(x=245, y=450)

        self.Image_3 = tk.PhotoImage(file='Images\Black_jeans.png')
        button = tk.Label(main_frame, image=self.Image_3, borderwidth=0).place(x=405, y=300)
        P3 = Product('Cl-192')
        tk.Button(main_frame,text='add',
                borderwidth=0, bg='#2d7aee',
                fg='#ffffff',width=5,
                command=P3.Add_Item).place(x=514, y=450)
        tk.Button(main_frame,text='remove',
                borderwidth=0,bg='#2d7aee',
                fg='#ffffff',
                command=P3.remove_Item).place(x=405, y=450)

        self.Image_4 = tk.PhotoImage(file='Images\Polo_shirt.png')
        button = tk.Label(main_frame, image=self.Image_4, borderwidth=0).place(x=565, y=300)
        P4 = Product('Cl-193')
        tk.Button(main_frame,text='add',
                borderwidth=0, bg='#2d7aee',
                fg='#ffffff',width=5,
                command=P4.Add_Item).place(x=674, y=450)
        tk.Button(main_frame,text='remove',
                borderwidth=0,bg='#2d7aee',
                fg='#ffffff',
                command=P4.remove_Item).place(x=565, y=450)

        self.Image_5 = tk.PhotoImage(file='Images\Denim_jacket.png')
        button = tk.Label(main_frame, image=self.Image_5, borderwidth=0).place(x=725, y=300)
        P5 = Product('Cl-194')
        tk.Button(main_frame,text='add',
                borderwidth=0, bg='#2d7aee',
                fg='#ffffff',width=5,
                command=P5.Add_Item).place(x=834, y=450)
        tk.Button(main_frame,text='remove',
                borderwidth=0,bg='#2d7aee',
                fg='#ffffff',
                command=P5.remove_Item).place(x=725, y=450)

class Cart:
    
    def configure_gui(self):
        self.cart_screen = tk.Tk()
        self.cart_screen.title('Cart')
        x = self.cart_screen.winfo_screenwidth() // 2 - 960 // 2
        y = self.cart_screen.winfo_screenheight() // 2 - 540 // 2
        self.cart_screen.geometry('960x540+%d+%d' % (x,y))
        self.cart_screen.resizable(FALSE,FALSE)
        self.Font_tuple = ('Open Sans', 9, 'bold')
        self.create_widgets()

    def create_widgets(self):

        main_frame = tk.Frame(self.cart_screen, bg='#f3f5f6')
        main_frame.place(x=0, y=0, width=960, height=540)

        check_frame = tk.Frame(main_frame,  bg='#3a3b42')
        check_frame.place(x=580, y=45, width=320, height=450)

        self.E_mail = tk.StringVar()
        self.First_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.address = tk.StringVar()
        self.Phone = tk.StringVar()
        self.City = tk.StringVar()

        tk.Label(main_frame, text='Contact information', bg='#f3f5f6', font=('Sans serif', 15, "bold")).place(x=42, y=45)
        tk.Label(main_frame, text='E-mail:', bg='#f3f5f6', font=self.Font_tuple).place(x=42, y=75)

        E_mail = tk.Entry(main_frame,
                            bg='lightgrey',
                            textvariable=self.E_mail,
                            borderwidth=0, width=45).place(x=45, y=100)
        

        tk.Label(main_frame, text='Shipping address', bg='#f3f5f6', font=('Sans serif', 15, "bold")).place(x=42, y=150)
        tk.Label(main_frame, text='First name:', bg='#f3f5f6', font=self.Font_tuple).place(x=42, y=180)

        First_name = tk.Entry(main_frame,
                            bg='lightgrey',
                            textvariable=self.First_name,
                            borderwidth=0, width=20).place(x=45, y=200)
        tk.Label(main_frame, text='Last name:', bg='#f3f5f6', font=self.Font_tuple).place(x=192, y=180)

        Last_name = tk.Entry(main_frame,
                            bg='lightgrey',
                            textvariable=self.last_name,
                            borderwidth=0, width=20).place(x=195, y=200)
        tk.Label(main_frame, text='Address:', bg='#f3f5f6', font=self.Font_tuple).place(x=42, y=220)

        Address = tk.Entry(main_frame,
                            bg='lightgrey',
                            textvariable=self.address,
                            borderwidth=0, width=45).place(x=45, y=240)
        tk.Label(main_frame, text='Phone:', bg='#f3f5f6', font=self.Font_tuple).place(x=42, y=260)

        Phone = tk.Entry(main_frame,
                            bg='lightgrey',
                            textvariable=self.Phone,
                            borderwidth=0, width=45).place(x=45, y=280)
        tk.Label(main_frame, text='City:', bg='#f3f5f6', font=self.Font_tuple).place(x=42, y=300)

        City = tk.Entry(main_frame,
                            bg='lightgrey',
                            textvariable=self.City,
                            borderwidth=0, width=45).place(x=45, y=320)
        tk.Label(check_frame,
                text='Reveiw Order',
                bg='#3a3b42', fg='#ffffff',
                font=self.Font_tuple).place(x=17, y=30)


        self.Back_icon = tk.PhotoImage(master=self.cart_screen, file = "Images\Back.png")
        tk.Button(main_frame,
                text = 'Continue Shopping',
                image = self.Back_icon,compound = LEFT,borderwidth=0,
                bg='#f3f5f6', fg='#2d7aee', font=self.Font_tuple,
                command=self.cart_screen.destroy).place(x=40, y=475, height=30)
        
        tk.Label(check_frame,text='Total =',bg='#3a3b42', fg='#ffffff').place(x=17, y=320)

        scrollbar = tk.Scrollbar(main_frame)
        scrollbar.pack(side=RIGHT, fill='y')
        textbox = tk.Text(check_frame,height=15,width=35)
        textbox.place(x=17,y=60)

        check_out = tk.Button(check_frame,
                            text='Check Out',
                            borderwidth=0, width=30,
                            bg='#2d7aee', fg='#ffffff', font=self.Font_tuple, command=self.check_out).place(x=50, y=375, height=30)

        try:
            df = pd.read_csv("Cart.txt")
            insert = df.to_string(index=False)
            textbox.insert(END,insert)
            z = df['Price'].sum()
            tk.Label(check_frame,text=str(z),bg='#3a3b42', fg='#ffffff').place(x=55, y=320)
        
        except:
            pass
        textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=textbox.yview)
        textbox.config(state='disabled')

    def check_out(self):
        User_data = []

        User_data.append(self.First_name.get())
        User_data.append(self.last_name.get())
        User_data.append(self.E_mail.get())
        User_data.append(self.address.get())
        User_data.append(self.Phone.get())
        User_data.append(self.City.get())
        
        def Order_id_gen():
            lower = string.ascii_lowercase
            upper = string.ascii_uppercase
            num = string.digits

            all = upper + num
            temp = random.sample(all,4)
            num =''.join(temp)

            today = date.today()
            dat = today.strftime("%Y-%m-%d")
            Order_id = "Order#:"+dat +"/"+ num
            User_data.append([Order_id])
 
        Order_id_gen()
        with open("Cart.txt") as f:
            reader = csv.reader(f)
            for row in reader:
                User_data.append(row)
        f.close()
        try:
            with open("History.txt","a",newline='') as f:
                writer = csv.writer(f)
                writer.writerows(User_data)
        except:
            pass

        def ExitApplication():
            MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
            if MsgBox == 'yes':
                df = pd.read_csv("Cart.txt")
                df = df.tail(df.shape[0] -100)
                df.to_csv("Cart.txt",index=False)
                
                self.cart_screen.destroy()
            else:
                messagebox.showinfo('Return','You will now return to the application screen')
        ExitApplication()


class Product:
    def __init__(self,product_id):
        self.Product_id = product_id

    def Add_Item(self):
        self.Product_list = []
        with open("Product_records.txt", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if self.Product_id == row[0]:
                    n = int(row[3])
                    stock = n-1
                    for field in row:
                        self.Product_list.append(field)
                    self.Product_list[3] = 1
                    df = pd.read_csv('Product_records.txt', index_col='Product-ID') 
                    df.loc[self.Product_id, 'Qty'] = stock
                    df.to_csv('Product_records.txt')

        with open("Cart.txt", "a",newline='') as f:
            writer = csv.writer(f)
            writer.writerows([self.Product_list])

        f.close()
        f.close()

    def remove_Item(self):
        with open("Product_records.txt", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    if self.Product_id == row[0]:
                        n = int(row[3])
                        if n < 50:
                            stock = n+1
                            df = pd.read_csv('Product_records.txt', index_col='Product-ID') 
                            df.loc[self.Product_id, 'Qty'] = stock
                            df.to_csv('Product_records.txt')
                except:
                    pass
        updated_data = []
        with open("Cart.txt", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if self.Product_id != row[0]:
                    updated_data.append(row)
                else:
                    Product_found = True
        f.close()
        try:
            if Product_found is True:
                with open("Cart.txt", "w",newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_data)
                f.close()
        except:
            pass

if __name__ == '__main__':
   master = tk.Tk()
   main_app = Main(master)
   master.mainloop()