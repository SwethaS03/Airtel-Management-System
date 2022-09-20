from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import *
import random
td=date.today()
d1=td.strftime("%d/%m/%Y")
conn = mysql.connector.connect(user='root', password='123', host='localhost', charset='utf8')
cursor = conn.cursor()
cursor.execute("create database if not exists tel")
cursor.execute("use tel")
cursor.execute("CREATE TABLE IF NOT EXISTS admin (username varchar(20), password varchar(20))")
cursor.execute("CREATE TABLE IF NOT EXISTS customer (customer_name varchar(20),customer_phone varchar(11),options varchar(10))")
cursor.execute("CREATE TABLE IF NOT EXISTS bill (bill_id varchar(6), customer_name varchar(20),mobilenum varchar(15),amount varchar(20),mop varchar(5),date varchar(15),options varchar(10))")
cursor.execute("SELECT * FROM admin WHERE username = 'admin' AND password = 'admin'")
if cursor.fetchone() is None:
    cursor.execute("INSERT INTO admin (username, password) VALUES('admin', 'admin')")
def mainloop(v):
    global root,loginpg,teleplans,telemenu,add,d1,window,nameentry,postpaid,prepaid,vbill,bill
    if v==1:
        root.destroy()
        loginpg = Tk()
        loginpg.title("MOBILE PHONE RECHARGE SYSTEM")
        loginpg.geometry("1300x650+0+0")
        loginpg.resizable(0,0)
        p2=PhotoImage(file='get4.png')
        l=Label(loginpg,image=p2).place(x=0,y=0)
        def call():
            loginpg.destroy()
            mainloop(10)
        p3=PhotoImage(file ='homeb.png').subsample(3,3)
        l=Button(loginpg,image=p3,relief=SOLID,command=call).place(x=1200,y=20)
        def login():
            if username.get() == "" or password.get() == "":
                messagebox.showinfo("msg","Please complete the required field!")
            else:
                cursor.execute("SELECT * FROM admin")
                b=cursor.fetchall()
                pl=[]
                for x in b:
                    for j in x:
                        pl.append(j)
                if username.get() == pl[0] or password.get() == pl[1]:
                    loginpg.destroy()
                    mainloop(3)
                else:
                    messagebox.showinfo("msg","Invalid username or password")
                    
        tele= Label(loginpg, text = "USERNAME:",fg='black',bg='white',font='arialblack 35 bold').place(x=320,y=200)            
        username = Entry(loginpg)
        username.configure(fg='black',font='arialblack 20 bold',relief="solid")
        username.place(x=650,y=200,height=50,width=300)

        tele= Label(loginpg, text = "PASSWORD:",fg='black',bg='white',font='arialblack 35 bold').place(x=320,y=270)    
        password = Entry(loginpg)
        password.configure(fg='black',font='arialblack 20 bold',show="*",relief="solid")
        password.place(x=650,y=270,height=50,width=300)
        submit=Button(loginpg,text="LOGIN",fg="black",bg="khaki2",font=("times","24","bold"),relief="solid",command=login).place(x=580,y=360)
        loginpg.mainloop()
    elif v==2:
        root.destroy()
        teleplans = Tk()
        teleplans.geometry("1300x650+0+0")
        teleplans.resizable(0,0)
        p2=PhotoImage(file='get3.png')
        l=Label(teleplans,image=p2).place(x=0,y=0)
        def call():
            teleplans.destroy()
            mainloop(10)
        p3=PhotoImage(file ='homeb.png').subsample(3,3)
        l=Button(teleplans,image=p3,relief=SOLID,command=call).place(x=1200,y=20)
        tele= Label(teleplans, text = "MOBILE RECHARGE PLANS",fg='black',bg='white',font='arialblack 40 bold').place(x=300,y=45)
        tele= Label(teleplans, text = "PACK",fg='black',bg='white',font='arialblack 30 bold').place(x=180,y=135)
        tele= Label(teleplans, text = "DATA",fg='black',bg='white',font='arialblack 30 bold').place(x=455,y=135)
        tele= Label(teleplans, text = "VALIDITY",fg='black',bg='white',font='arialblack 30 bold').place(x=700,y=135)
        tele= Label(teleplans, text = "CALLS",fg='black',bg='white',font='arialblack 30 bold').place(x=1000,y=135)
        tele1= Label(teleplans, text = "Rs.598 pack",fg='blue',bg='white',font='arialblack 20 bold').place(x=145,y=217)
        tele1= Label(teleplans, text ="1.5GB/day",fg='black',bg='white',font='arialblack 20 bold').place(x=435,y=217)
        tele1= Label(teleplans, text ="84 days",fg='black',bg='white',font='arialblack 20 bold').place(x=735,y=217)
        tele1= Label(teleplans, text ="unlimited calls",fg='red',bg='white',font='arialblack 20 bold').place(x=965,y=217)
        tele2= Label(teleplans, text = "Rs.449 pack",fg='blue',bg='white',font='arialblack 20 bold').place(x=145,y=290)
        tele2= Label(teleplans, text ="2.0GB/day",fg='black',bg='white',font='arialblack 20 bold').place(x=435,y=290) 
        tele2= Label(teleplans, text ="56 days",fg='black',bg='white',font='arialblack 20 bold').place(x=735,y=290)
        tele2= Label(teleplans, text ="unlimited calls",fg='red',bg='white',font='arialblack 20 bold').place(x=965,y=290)
        tele3= Label(teleplans, text = "Rs.298 pack",fg='blue',bg='white',font='arialblack 20 bold').place(x=145,y=363)
        tele3= Label(teleplans, text ="2.0GB/day",fg='black',bg='white',font='arialblack 20 bold').place(x=435,y=363)
        tele3= Label(teleplans, text ="28 days",fg='black',bg='white',font='arialblack 20 bold').place(x=735,y=363)
        tele3= Label(teleplans, text ="unlimited calls",fg='red',bg='white',font='arialblack 20 bold').place(x=965,y=363)
        tele4= Label(teleplans, text = "Rs.399 pack",fg='blue',bg='white',font='arialblack 20 bold').place(x=145,y=436)
        tele4= Label(teleplans, text ="1.5GB/day",fg='black',bg='white',font='arialblack 20 bold').place(x=435,y=436)
        tele4= Label(teleplans, text ="56 days",fg='black',bg='white',font='arialblack 20 bold').place(x=735,y=436)
        tele4= Label(teleplans, text ="unlimited calls",fg='red',bg='white',font='arialblack 20 bold').place(x=965,y=436)
        tele5= Label(teleplans, text = "Rs.149 pack",fg='blue',bg='white',font='arialblack 20 bold').place(x=145,y=499)
        tele5= Label(teleplans, text ="1.0GB/day",fg='black',bg='white',font='arialblack 20 bold').place(x=435,y=499)
        tele5= Label(teleplans, text ="28 days ",fg='black',bg='white',font='arialblack 20 bold').place(x=735,y=499)
        tele5= Label(teleplans, text ="free incoming calls",fg='red',bg='white',font='arialblack 20 bold').place(x=935,y=499)
        teleplans.mainloop()

    elif v==3:
        telemenu = Tk()
        telemenu.geometry("1300x650+0+0")
        telemenu.resizable(0,0)
        p1=PhotoImage(file='get5.png')
        l=Label(telemenu,image=p1).place(x=0,y=0)
        def call():
            telemenu.destroy()
            mainloop(10)
        prepaid=Button(telemenu,text='Pay Bill Prepaid',bg='white',fg='black',font='arialblack 20 bold',relief="solid",command=lambda:mainloop(5)).place(x=100,y=250,height=50,width=300)
        postpaid=Button(telemenu,text='Pay Bill Postpaid',bg='white',fg='black',font='arialblack 20 bold',relief="solid",command=lambda:mainloop(6)).place(x=500,y=250,height=50,width=300)
        addnum=Button(telemenu,text='Add New Customer',bg='white',fg='black',font='arialblack 20 bold',relief="solid",command=lambda:mainloop(4)).place(x=900,y=250,height=50,width=300)
        dailyamt=Button(telemenu,text='Todays Payments',bg='white',fg='black',font='arialblack 20 bold',relief="solid",command=lambda:mainloop(8)).place(x=275,y=350,height=50,width=300)
        customer=Button(telemenu,text='View Customers',bg='white',fg='black',font='arialblack 20 bold',relief="solid",command=lambda:mainloop(7)).place(x=675,y=350,height=50,width=300)
        b=Button(telemenu,text='LOGOUT',font='arialblack 20 bold',bg='white',fg='black',relief="solid",command=call).place(x=1100,y=40,height=50,width=150)
        telemenu.mainloop()
    elif v==4:
        telemenu.destroy()
        add=Tk()
        add.geometry("1300x650+0+0")
        add.resizable(0,0)
        p1=PhotoImage(file='get7.png')
        l=Label(add,image=p1).place(x=0,y=0)
        def call():
            add.destroy()
            mainloop(3)
        p3=PhotoImage(file ='homeb.png').subsample(3,3)
        l=Button(add,image=p3,relief=SOLID,command=call).place(x=1200,y=20)

        def save():
            na=custname.get()
            nu=custnum.get()
            v1=var1.get()
            v2=var2.get()
            if v1==1 and v2==0:
                a='prepaid'
                k="insert into customer values('{}','{}','{}')".format(na,nu,a)
                cursor.execute(k)
                conn.commit()
                add.destroy()
                mainloop(3)
            elif v2==1 and v1==0:
                a='postpaid'
                k="insert into customer values('{}','{}','{}')".format(na,nu,a)
                cursor.execute(k)
                conn.commit()
                add.destroy()
                mainloop(3)
            else:
                messagebox.showinfo("msg","select prepaid/postpaid")
            
        tele= Label(add, text = "NAME:",fg='black',bg='white',font='arialblack 30 bold').place(x=320,y=180)            
        custname = Entry(add)
        custname.configure(fg='black',font='arialblack 20 bold',relief="solid")
        custname.place(x=680,y=180,height=50,width=300)
        
        tele= Label(add, text = "MOBILE NUMBER:",fg='black',bg='white',font='arialblack 30 bold').place(x=320,y=250)    
        custnum = Entry(add)
        custnum.configure(fg='black',font='arialblack 20 bold',relief="solid")
        custnum.place(x=680,y=250,height=50,width=300)

        var1 = IntVar()
        Checkbutton(add, text="Prepaid", variable=var1,font='arailblack 20 bold',bg='white').place(x=400,y=310)
        var2 = IntVar()
        Checkbutton(add, text="Postpaid", variable=var2,font='arialblack 20 bold',bg='white').place(x=730,y=310)
        submit=Button(add,text="SAVE",fg="black",bg="khaki2",font=("times","24","bold"),relief="solid",command=save).place(x=580,y=370)

        add.mainloop()
    elif v==5:
        global search,Number
        telemenu.destroy()
        prepaid=Tk()
        prepaid.geometry("1300x650+0+0")
        p2=PhotoImage(file='get8.png')
        l=Label(prepaid,image=p2).place(x=0,y=0)
        def call():
            prepaid.destroy()
            mainloop(3)
        p3=PhotoImage(file ='homeb.png').subsample(3,3)
        l=Button(prepaid,image=p3,relief=SOLID,command=call).place(x=1200,y=20)

        def payb():
            global Name,Amount,Number,var1,var2
            na=Name.get()
            nu=Number.get()
            am=Amount.get()
            v1=var1.get()
            v2=var2.get()
            op='prepaid'
            bid='AB'+str(random.randint(100,999))
            if v1==1 and v2==0:
                a='cash'
                k="insert into bill values('{}','{}','{}','{}','{}','{}','{}')".format(bid,na,nu,am,a,d1,op)
                cursor.execute(k)
                conn.commit()
                prepaid.destroy()
                mainloop(9)
            elif v2==1 and v1==0:
                a='card'
                k="insert into bill values('{}','{}','{}','{}','{}','{}','{}')".format(bid,na,nu,am,a,d1,op)
                cursor.execute(k)
                conn.commit()
                prepaid.destroy()
                mainloop(9)
            else:
                messagebox.showinfo("msg","select cash/card")
        def searchh():
            global Name,Amount,var1,var2
            n=Number.get()
            k=('select customer_name,customer_phone from customer where customer_phone=%s and options="prepaid"'%n)
            cursor.execute(k)
            b=cursor.fetchall()
            if b==[]:
                messagebox.showinfo("msg","enter registered number/prepaid number")
            else:
                up=[]
                for x in b:
                    for j in x:
                        up.append(j)
                if n==up[1]:
                    search.destroy()
                    Name = Entry(prepaid)
                    Name.insert(0,up[0])
                    Name.configure(fg='black',font='arialblack 25 bold')
                    name=Label(prepaid,text="Name",fg='black',bg='white',font='arialblack 25 bold').place(x=400,y=200)
                    Name.place(x=600,y=200,height=35,width=300)
                
                    Amount = Entry(prepaid)
                    Amount.configure(fg='black',font='arialblack 25 bold')
                    Amt=Label(prepaid,text='Amount',fg='black',bg='white',font='arialblack 25 bold').place(x=400,y=275)
                    Amount.place(x=600,y=275,height=35,width=300)
                    var1 = IntVar()
                    Checkbutton(prepaid, text="Cash", variable=var1,font='arailblack 20 bold',bg='white').place(x=540,y=340)
                    var2 = IntVar()
                    Checkbutton(prepaid, text="Card", variable=var2,font='arialblack 20 bold',bg='white').place(x=700,y=340)
                    pay=Button(prepaid,text="Pay bill",fg="black",bg="white",font='arialblack 25 bold',width=7,command=payb).place(x=550,y=410)
                else:
                    messagebox.showinfo("msg","enter registered number")
        Number = Entry(prepaid)
        Number.configure(fg='black',font='arialblack 25 bold')
        num=Label(prepaid,text='Number',fg='black',bg='white',font='arialblack 25 bold').place(x=400,y=125)
        Number.place(x=600,y=125,height=35,width=300)
        search=Button(prepaid,text="SEARCH",fg="black",bg="white",font='arialblack 25 bold',width=7,command=searchh)
        search.place(x=600,y=200)
        prepaid.mainloop()
        
    elif v==6:
        telemenu.destroy()
        postpaid=Tk()
        postpaid.geometry("1300x650+0+0")
        p2=PhotoImage(file='get9.png')
        l=Label(postpaid,image=p2).place(x=0,y=0)
        def call():
            postpaid.destroy()
            mainloop(3)
        p3=PhotoImage(file ='homeb.png').subsample(3,3)
        l=Button(postpaid,image=p3,relief=SOLID,command=call).place(x=1200,y=20)
        
        def paybp():
            global Namep,Amountp,Numberp,var1p,var2p
            nap=Namep.get()
            nup=np
            amp=Amountp.get()
            v1p=var1p.get()
            v2p=var2p.get()
            opp='postpaid'
            bidp='AB'+str(random.randint(100,999))
            if v1p==1 and v2p==0:
                a='cash'
                k="insert into bill values('{}','{}','{}','{}','{}','{}','{}')".format(bidp,nap,nup,amp,a,d1,opp)
                cursor.execute(k)
                conn.commit()
                postpaid.destroy()
                mainloop(9)
            elif v2p==1 and v1p==0:
                a='card'
                k="insert into bill values('{}','{}','{}','{}','{}','{}','{}')".format(bidp,nap,nup,amp,a,d1,opp)
                cursor.execute(k)
                conn.commit()
                postpaid.destroy()
                mainloop(9)
            else:
                messagebox.showinfo("msg","select cash/card")
        def searchp():
            global Namep,Amountp,var1p,var2p,np
            np=Numberp.get()
            k=('select customer_name,customer_phone from customer where customer_phone=%s and options="postpaid"'%np)
            cursor.execute(k)
            b=cursor.fetchall()
            if b==[]:
                messagebox.showinfo("msg","enter registered number/postpaid number")
            else:
                up=[]
                for x in b:
                    for j in x:
                        up.append(j)
                if np==up[1]:
                    searchp.destroy()
                    Namep = Entry(postpaid)
                    Namep.insert(0,up[0])
                    Namep.configure(fg='black',font='arialblack 25 bold')
                    namep=Label(postpaid,text="Name",fg='black',bg='white',font='arialblack 25 bold').place(x=400,y=200)
                    Namep.place(x=600,y=200,height=35,width=300)
                    c=random.randint(250,350)
                    c=c*1.5+200
                    Amountp = Entry(postpaid)
                    Amountp.insert(0,c)
                    Amountp.configure(fg='black',font='arialblack 25 bold')
                    Amtp=Label(postpaid,text='Amount',fg='black',bg='white',font='arialblack 25 bold').place(x=400,y=275)
                    Amountp.place(x=600,y=275,height=35,width=300)
                    var1p = IntVar()
                    Checkbutton(postpaid, text="Cash", variable=var1p,font='arailblack 20 bold',bg='white').place(x=540,y=340)
                    var2p = IntVar()
                    Checkbutton(postpaid, text="Card", variable=var2p,font='arialblack 20 bold',bg='white').place(x=700,y=340)
                    payp=Button(postpaid,text="Pay bill",fg="black",bg="white",font='arialblack 25 bold',width=7,command=paybp).place(x=550,y=410)
                else:
                    messagebox.showinfo("msg","enter registered number")
        
        Numberp = Entry(postpaid)
        Numberp.configure(fg='black',font='arialblack 25 bold')
        nump=Label(postpaid,text='Number',fg='black',bg='white',font='arialblack 25 bold').place(x=400,y=125)
        Numberp.place(x=600,y=125,height=35,width=300)
        searchp=Button(postpaid,text="SEARCH",fg="black",bg="white",font='arialblack 25 bold',width=7,command=searchp)
        searchp.place(x=600,y=200)
        
        postpaid.mainloop()
        
    elif v==7:
        telemenu.destroy()
        window = Tk()
        window.geometry("1300x650+0+0")
        p1=PhotoImage(file='get11.png')
        l=Label(window,image=p1).place(x=0,y=0)
        def call():
            window.destroy()
            mainloop(3)
        p3=PhotoImage(file ='homeb.png').subsample(3,3)
        l=Button(window,image=p3,relief=SOLID,command=call).place(x=1200,y=15)

        updateTV=ttk.Treeview(height=15,columns=('Name','Number','Options'))
        nameentry=StringVar()
        custTV=ttk.Treeview(height=15,columns=('Name','Number','Options'))

        def getcustdata():
            records=updateTV.get_children()
            
            for j in records:
                upadateTV.delete(j)
                       
            conn=mysql.connector.connect(host='localhost',user='root',passwd='123',db='tel',charset='utf8')
            cursor=conn.cursor(dictionary=True)
            query='select * from customer'
            cursor.execute(query)
            data=cursor.fetchall()
                
            for i in data:
                updateTV.insert('','end',text=i['customer_name'],values=(i['customer_phone'],i['options']))
            conn.close()        

        def searching():
            global nameentry
            name=nameentry.get()
            
            records=custTV.get_children()    
            for j in records:
                custTV.delete(j)
                       
            conn=mysql.connector.connect(host='localhost',user='root',passwd='123',db='tel',charset='utf8')
            cursor=conn.cursor(dictionary=True)
            query='select * from customer where customer_name="{}"'.format(name)
            cursor.execute(query)
            data=cursor.fetchall()
            
            for i in data:
                custTV.insert('','end',text=i['customer_name'],values=(i['customer_phone'],i['options']))
            conn.close()          

            
        def getdata():  
            global nameentry

            b=Entry(window,textvariable=nameentry)
            b.place(x=100,y=140,width=300,height=50)

            c=Button(window,text='search',command=searching)
            c.place(x=100,y=200,width=300,height=50)  
            
            updateTV.place(x=500,y=50,width=760,height=560)

            scrollBar1 = Scrollbar(window, orient="vertical",command=updateTV.yview)
            scrollBar1.place(x=1258,y=50,height=560)

            updateTV.configure(yscrollcommand=scrollBar1.set)
            
            updateTV.heading('#0',text='Name')
            updateTV.column('#0',minwidth=0,width=253,anchor='center')
            updateTV.heading('#1',text="Number")
            updateTV.column('#1', minwidth=0, width=253,anchor='center')
            updateTV.heading('#2',text='Options')
            updateTV.column('#2',minwidth=0,width=254,anchor='center')
            getcustdata()

            custTV.place(x=20,y=260,width=450,height=350)

            scrollBar2 = Scrollbar(window, orient="vertical",command=custTV.yview)
            scrollBar2.place(x=468,y=260,height=350)

            updateTV.configure(yscrollcommand=scrollBar2.set)
            
            custTV.heading('#0',text='Name')
            custTV.column('#0',minwidth=0,width=150,anchor='center')
            custTV.heading('#1',text="Number")
            custTV.column('#1', minwidth=0, width=150,anchor='center')
            custTV.heading('#2',text='Options')
            custTV.column('#2',minwidth=0,width=150,anchor='center')
        getdata()
        window.mainloop()
    elif v==8:
        telemenu.destroy()
        vbill = Tk()
        vbill.geometry("1300x650+0+0")

        p1=PhotoImage(file='get10.png')
        l=Label(vbill,image=p1).place(x=0,y=0)
        def call():
            vbill.destroy()
            mainloop(3)
        p3=PhotoImage(file ='homeb.png').subsample(3,3)
        l=Button(vbill,image=p3,relief=SOLID,command=call).place(x=1200,y=20)

        viewTV=ttk.Treeview(height=20,columns=('Bill ID','Name','Number','Amount','MOP','Date','Options'))

        def getallcustdata():
            records=viewTV.get_children()
            
            for j in records:
                viewTV.delete(j)
                
            conn=mysql.connector.connect(host='localhost',user='root',passwd='123',db='tel',charset='utf8')
            cursor=conn.cursor(dictionary=True)
            query='select * from bill'
            cursor.execute(query)
            data=cursor.fetchall()
                
            for i in data:
                viewTV.insert('','end',text=i['bill_id'],values=(i['customer_name'],i['mobilenum'],i['amount'],i['mop'],i['date'],i['options']))
            conn.close()        

        def displayallcust():
            viewTV.place(x=20,y=100,width=1240,height=525)

            scrollBar3 = Scrollbar(vbill, orient="vertical",command=viewTV.yview)
            scrollBar3.place(x=1258,y=100,height=525)

            viewTV.configure(yscrollcommand=scrollBar3.set)
            
            viewTV.heading('#0',text='Bill ID')
            viewTV.column('#0',minwidth=0,width=178,anchor='center')
            viewTV.heading('#1',text="Name")
            viewTV.column('#1', minwidth=0, width=178,anchor='center')
            viewTV.heading('#2',text='Number')
            viewTV.column('#2',minwidth=0,width=180,anchor='center')
            viewTV.heading('#3',text='Amount')
            viewTV.column('#3',minwidth=0,width=178,anchor='center')
            viewTV.heading('#4',text='MOP')
            viewTV.column('#4',minwidth=0,width=178,anchor='center')
            viewTV.heading('#5',text='Date')
            viewTV.column('#5',minwidth=0,width=180,anchor='center')
            viewTV.heading('#6',text='Options')
            viewTV.column('#6',minwidth=0,width=178,anchor='center')
            
            getallcustdata()

        displayallcust()
        vbill.mainloop()
    elif v==9:
        bill=Tk()
        bill.geometry("1300x650+0+0")
        p2=PhotoImage(file='table.png')
        l=Label(bill,image=p2).place(x=0,y=0)
        
        k='select * from bill'
        cursor.execute(k)
        b=cursor.fetchall()
        up=[]
        for x in range(0,len(b)):
            if x==(len(b)-1):
                for j in b[x]:
                    up.append(j)
        def call():
            bill.destroy()
            mainloop(3)
        pay=Label(bill,text="Bill no:",fg='black',bg='white',font='arialblack 30 bold').place(x=310,y=95)
        pay=Label(bill,text=up[0],fg='black',bg='white',font='arialblack 30 bold').place(x=660,y=95)
        name=Label(bill,text="Name:",fg="black",bg="white",font='arialblack 30 bold').place(x=310,y=165)
        name=Label(bill,text=up[1],fg="black",bg="white",font='arialblack 30 bold').place(x=660,y=165)
        num=Label(bill,text="Number:",fg="black",bg="white",font='arialblack 30 bold').place(x=310,y=235)
        num=Label(bill,text=up[2],fg="black",bg="white",font='arialblack 30 bold').place(x=660,y=235)
        pack=Label(bill,text="Date:",fg="black",bg="white",font='arialblack 30 bold').place(x=310,y=305)
        pack=Label(bill,text=up[5],fg="black",bg="white",font='arialblack 30 bold').place(x=660,y=305)
        amount=Label(bill,text="Amount:",fg="black",bg="white",font='arialblack 30 bold').place(x=310,y=375)
        amount=Label(bill,text=up[3],fg="black",bg="white",font='arialblack 30 bold').place(x=660,y=375)
        mode=Label(bill,text="Mode of payment:",fg="black",bg="white",font='arialblack 28 bold').place(x=310,y=445)
        mode=Label(bill,text=up[4],fg="black",bg="white",font='arialblack 30 bold').place(x=660,y=445)
        printbill=Button(bill,text='Print Bill',fg='black',bg='white',font='arialblack 30 bold',relief='solid',command=call).place(x=540,y=530)
        bill.mainloop()
    else:
        root = Tk()
        root.title("MOBILE PHONE RECHARGE SYSTEM")
        root.geometry("1300x650+0+0")
        root.resizable(0,0)
        p1=PhotoImage(file='get1.png')
        l=Label(root,image=p1).place(x=0,y=0)

        lb=Button(root,text='ADMIN LOGIN',bg='white',fg='red',font='arialblack 30 bold',relief="solid",command=lambda:mainloop(1)).place(x=900,y=250)

        lb=Button(root,text='VIEW PLANS',bg='white',fg='red',font='arialblack 30 bold',relief="solid",command=lambda:mainloop(2)).place(x=910,y=350)
        root.mainloop()
        
mainloop(10)

