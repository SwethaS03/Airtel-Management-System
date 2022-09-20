from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector 
import tkinter.ttk as ttk
root = Tk()
root.title("Telephone Billing System")

width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#8EE4AF")

#========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
CUSTOMER_NAME = StringVar()
CUSTOMER_ADDRESS =StringVar()
CUSTOMER_PHONE = StringVar()
MOBILE = StringVar()
STD = StringVar()
ISD = StringVar()
#CUSTOMER_NAME = StringVar()
MOBILE_AMT = StringVar()
STD_AMT = StringVar()
SEARCH = StringVar()

#========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = mysql.connector.connect(user='root', password='123', host='localhost', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("create database if not exists tel")
    cursor.execute("use tel")
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id int(3), username varchar(20), password varchar(20))")
    cursor.execute("CREATE TABLE IF NOT EXISTS `customer` (customer_id int(10), customer_name varchar(20), customer_address varchar(20), customer_phone varchar(15))")
    cursor.execute("CREATE TABLE IF NOT EXISTS `bill` (bill_id int(3), customer_name varchar(20),mobileamt varchar(15),stdamt varchar(20))")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def entry():
    global uname,pswd,lbl_result
    uname=username.get()
    pswd=password.get()
    cursor=mydb.cursor()
    cursor.execute("select pswd from admin where username='{}' and password='{}'".format(uname,pswd))
    data=cursor.fetchall()
    up=[]
    for x in data:
        for j in x:
            up.append(j)
    if pswd in up:
        Home1()
    else:
         lbl_result.config(text="Invalid username or password", fg="red")

def enter1():
    username = Entry(enter1)
    username.configure(fg='black',font='arialblack 18 bold')
    username.place(x=650,y=250,height=40,width=300)
        
    password = Entry(enter)
    password.configure(fg='black',font='arialblack 18 bold',show="*")
    password.place(x=650,y=350,height=40,width=300)
    submit=Button(enter1,text="SUBMIT",fg="black",bg="khaki2",font=("times","24","bold"),width=7,activebackground="khaki4",command=entry).place(x=500,y=450)

##rootw=Tk()
##rootw.geometry("700x700")
##rootw.configure(bg="white")
##rootw.title("admin page")
##ca=photoimage(open(file=path))
##w=label(rootw,image=ca)
##w.place(x=0,y=0)



def Exit():
    result = tkMessageBox.askquestion('Telephone Billing System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    result = tkMessageBox.askquestion('Telephone Billing System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()

def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Telephone Billing System/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()
    
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)
    
def Home():
    global Home
    Home = Tk()
    Home.title("Telephone Billing System/Home")
    width = 1024
    height = 520
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Telephone Billing System", font=('arial', 45))
    lbl_display.pack()
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Add new", command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowView)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Customer Details", menu=filemenu2)
    filemenu2.add_command(label="bill", command=ShowAddNew2)
    filemenu2.add_command(label="View", command=ShowView2)
    Home.config(menu=menubar)
    Home.config(bg="#8D8741")

def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Telephone Billing System/Add new")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()

def ShowAddNew1():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Telephone Billing System/Add new")
    width = 600
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm1()


def ShowAddNew2():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Telephone Billing System/Add new")
    width = 600
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm2()

def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Product", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_customername = Label(MidAddNew, text="Customer Name:", font=('arial', 25), bd=10)
    lbl_customername.grid(row=0, sticky=W)
    lbl_address = Label(MidAddNew, text="Customer Address:", font=('arial', 25), bd=10)
    lbl_address.grid(row=1, sticky=W)
    lbl_phone = Label(MidAddNew, text="Customer Phone:", font=('arial', 25), bd=10)
    lbl_phone.grid(row=2, sticky=W)
    customername = Entry(MidAddNew, textvariable=CUSTOMER_NAME, font=('arial', 25), width=15)
    customername.grid(row=0, column=1)
    mobileamt = Entry(MidAddNew, textvariable=CUSTOMER_ADDRESS, font=('arial', 25), width=15)
    mobileamt.grid(row=1, column=1)
    stdamt = Entry(MidAddNew, textvariable=CUSTOMER_PHONE, font=('arial', 25), width=15)
    stdamt.grid(row=2, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew)
    btn_add.grid(row=3, columnspan=2, pady=20)
    
def AddNewForm1():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Rates", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_mobile = Label(MidAddNew, text="Mobile :", font=('arial', 25), bd=10)
    lbl_mobile.grid(row=0, sticky=W)
    lbl_std = Label(MidAddNew, text="Std:", font=('arial', 25), bd=10)
    lbl_std.grid(row=1, sticky=W)
    lbl_isd = Label(MidAddNew, text="Isd:", font=('arial', 25), bd=10)
    lbl_isd.grid(row=2, sticky=W)
    mobile = Entry(MidAddNew, textvariable=MOBILE, font=('arial', 25), width=15)
    mobile.grid(row=0, column=1)
    std = Entry(MidAddNew, textvariable=STD, font=('arial', 25), width=15)
    std.grid(row=1, column=1)
    isd = Entry(MidAddNew, textvariable=ISD, font=('arial', 25), width=15)
    isd.grid(row=2, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew1)
    btn_add.grid(row=3, columnspan=2, pady=20)

def AddNewForm2():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Product", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_customername = Label(MidAddNew, text="Customer Name:", font=('arial', 25), bd=10)
    lbl_customername.grid(row=0, sticky=W)
    lbl_address = Label(MidAddNew, text="Mobile Amount:", font=('arial', 25), bd=10)
    lbl_address.grid(row=1, sticky=W)
    lbl_phone = Label(MidAddNew, text="Std Amount:", font=('arial', 25), bd=10)
    lbl_phone.grid(row=2, sticky=W)
    customername = Entry(MidAddNew, textvariable=CUSTOMER_NAME, font=('arial', 25), width=15)
    customername.grid(row=0, column=1)
    mobileamt = Entry(MidAddNew, textvariable=MOBILE_AMT, font=('arial', 25), width=15)
    mobileamt.grid(row=1, column=1)
    stdamt = Entry(MidAddNew, textvariable=STD_AMT, font=('arial', 25), width=15)
    stdamt.grid(row=2, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew2)
    btn_add.grid(row=3, columnspan=2, pady=20)
      


def AddNew():
    Database()
    cursor.execute("INSERT INTO `customer` (customer_name, customer_Address, customer_phone) VALUES(%s, %s, %s)", (str(CUSTOMER_NAME.get()), str(CUSTOMER_ADDRESS.get()), str(CUSTOMER_PHONE.get())))
    conn.commit()
    CUSTOMER_NAME.set("")
    CUSTOMER_ADDRESS.set("")
    CUSTOMER_PHONE.set("")
    cursor.close()
    conn.close()
    
def AddNew2():
    Database()
    cursor.execute("INSERT INTO `bill` (customer_name, mobileamt, stdamt) VALUES(%s, %s, %s)", (str(CUSTOMER_NAME.get()), str(MOBILE_AMT.get()), str(STD_AMT.get())))
    conn.commit()
    CUSTOMER_NAME.set("")
    #CUSTOMER_ADDRESS.set("")
    #CUSTOMER_PHONE.set("")
    MOBILE_AMT.set("")
    STD_AMT.set("")
    #ISD_AMT.set("")
    cursor.close()
    conn.close()


def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Customers", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    #btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("CustomerID", "Customer Name", "Customer Address", "Customer Phone"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('CustomerID', text="ProductID",anchor=W)
    tree.heading('Customer Name', text="Customer Name",anchor=W)
    tree.heading('Customer Address', text="Customer Address",anchor=W)
    tree.heading('Customer Phone', text="Customer Phone",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

def ViewForm1():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Call rates", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search1)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset1)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete1)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("CallerID", "Mobile", "Std","Isd"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('CallerID', text="CallerID",anchor=W)
    #tree.heading('Local', text="Local",anchor=W)
    tree.heading('Mobile', text="Mobile",anchor=W)
    tree.heading('Std', text="Std",anchor=W)
    tree.heading('Isd', text="Isd",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData1()

def ViewForm2():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Bill", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search2)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset2)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("BillID", "Customer Name", "Mobile Amount", "Std Amount"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('BillID', text="BillID",anchor=W)
    tree.heading('Customer Name', text="Customer Name",anchor=W)
    tree.heading('Mobile Amount', text="Mobile Amount",anchor=W)
    tree.heading('Std Amount', text="Std Amount",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData2()
    
def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `customer`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def DisplayData2():
    Database()
    cursor.execute("SELECT * FROM `bill`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `customer` WHERE `customer_name` LIKE %s", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Search1():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `callrates` WHERE local` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Search2():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `bill` WHERE `customer_name` LIKE %s", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")
    
def Reset2():
    tree.delete(*tree.get_children())
    DisplayData2()
    SEARCH.set("")


##def Delete():
##    global tree
##    if not tree.selection():
##       print("ERROR")
##    else:
##        result = tkMessageBox.askquestion('Telephone Billing System', 'Are you sure you want to delete this record?', icon="warning")
##        if result == 'yes':
##            curItem = tree.focus()
##            contents =(tree.item(curItem))
##            selecteditem = contents['values']
##            tree.delete(curItem)
##            Database()
##            cursor.execute("DELETE FROM `customer` WHERE `customer_id` = %d" % selecteditem[0])
##            conn.commit()
##            cursor.close()
##            conn.close()
##Delete()
##
##def Delete1():
##    global tree
##    if not tree.selection():
##       print("ERROR")
##    else:
##        result = tkMessageBox.askquestion('Telephone Billing System', 'Are you sure you want to delete this record?', icon="warning")
##        if result == 'yes':
##            curItem = tree.focus()
##            contents =(tree.item(curItem))
##            selecteditem = contents['values']
##            tree.delete(curItem)
##            Database()
##            cursor.execute("DELETE FROM `callrates` WHERE `customer_id` = %d" % selecteditem[0])
##            conn.commit()
##            cursor.close()
##            conn.close()
##Delete1()
##
##def Delete2():
##    global tree
##    if not tree.selection():
##       print("ERROR")
##    else:
##        result = tkMessageBox.askquestion('Telephone Billing System', 'Are you sure you want to delete this record?', icon="warning")
##        if result == 'yes':
##            curItem = tree.focus()
##            contents =(tree.item(curItem))
##            selecteditem = contents['values']
##            tree.delete(curItem)
##            Database()
##            cursor.execute("DELETE FROM `bill` WHERE `bill_id` = %d" % selecteditem[0])
##            conn.commit()
##            cursor.close()
##            conn.close()
##Delete2()
   

def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Telephone Billing System/View Customer")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()

def ShowView1():
    global viewform
    viewform = Toplevel()
    viewform.title("Telephone Billing System/View Product")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm1()

def ShowView2():
    global viewform
    viewform = Toplevel()
    viewform.title("Telephone Billing System/View bill")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm2()

def Logout():
    result = tkMessageBox.askquestion('Telephone Billing System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes': 
        admin_id = ""
        root.deiconify()
        Home.destroy()
  
def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = %s AND `password` = %s", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = %s AND `password` = %s", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close() 

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()


#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=1)
filemenu.add_command(label="Admin Login", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

#========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

#========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="Telephone Billing System", font=('arial', 45))
lbl_display.pack()

#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
