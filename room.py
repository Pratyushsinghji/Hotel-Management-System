from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x500+180+70")

        #===============varibles==============
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noOfdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        

        # ===============title==================
        Ibl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        Ibl_title.place(x=0, y=0, width=1295, height=50)


        # ===============logo==================
        img2 = Image.open(r"D:\Coding\python\Hotel Management\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbl_img2.place(x=5, y=2, width=100, height=40)

        # ===============label frame=============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # ===============label and entrys=============
        # Customer Contact
        Ibl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("times new roman",12,"bold"),padx=2,pady=6)
        Ibl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("times new roman",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        # Fetch Data button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial", 8, "bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)

        # Check_In Date
        check_in_date=Label(labelframeleft,text="Check_In Date",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkin,font=("times new roman",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        # Check_Out Date
        Ibl_check_out=Label(labelframeleft,text="Check_Out Date",font=("times new roman",12,"bold"),padx=2,pady=6)
        Ibl_check_out.grid(row=2,column=0,sticky=W)

        txt_check_out=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkout,font=("times new roman",13,"bold"))
        txt_check_out.grid(row=2,column=1)

        # Room Type
        label_RoomType=Label (labelframeleft, font=("arial", 12, "bold"), text="Room Type :",padx=2,pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()
        

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("arial",12,"bold"), width=27, state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable=Label (labelframeleft, font=("arial", 12, "bold"), text="Available Room: ", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        lblRoomAvailable=ttk. Entry (labelframeleft,textvariable=self.var_roomavailable,font=("arial", 13, "bold"), width=29)
        lblRoomAvailable.grid(row=4, column=1)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable, font=("arial",12,"bold"), width=27, state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # Meal
        lblMeal=Label(labelframeleft, font=("arial",12,"bold"),text="Meal:", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal=ttk.Entry (labelframeleft,textvariable=self.var_meal,font=("arial", 13, "bold"),width=29)
        txtMeal.grid(row=5, column=1)

        # No Of Days
        IblNoOfDays=Label (labelframeleft, font=("arial", 12, "bold"), text="No Of Days: ", padx=2,pady=6)
        IblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays=ttk.Entry (labelframeleft,textvariable=self.var_noOfdays,font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        IblPaidTax=Label (labelframeleft, font=("arial", 12, "bold"), text="Paid Tax: ", padx=2,pady=6)
        IblPaidTax.grid(row=7, column=0, sticky=W)
        txtPaidTax=ttk.Entry (labelframeleft,textvariable=self.var_paidtax,font=("arial", 13, "bold"), width=29)
        txtPaidTax.grid(row=7, column=1)

        # Sub Total
        lblSubTotal=Label(labelframeleft, font=("arial",12,"bold"),text="Sub Total:", padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)
        txtSubTotal=ttk.Entry (labelframeleft,textvariable=self.var_actualtotal, font=("arial", 13, "bold"),width=29)
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        IblTotalCost=Label (labelframeleft, font=("arial", 12, "bold"), text="Total Cost: ", padx=2,pady=6)
        IblTotalCost.grid(row=9, column=0, sticky=W)
        txtTotalCost=ttk.Entry (labelframeleft,textvariable=self.var_total,font=("arial", 13, "bold"), width=29)
        txtTotalCost.grid(row=9, column=1)

        #======================Bill Button====================
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        # ===============btns===============
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnUpdate .grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #==============Rightside image==============
        img3 = Image.open(r"D:\Coding\python\Hotel Management\hotel images\bed.jpg")
        img3 = img3.resize((520, 200), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_img3 = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lbl_img3.place(x=760, y=55, width=520, height=200)


        # ===============tabel frame search system=============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label (Table_Frame, font=("arial", 12, "bold"), text="Search By :",bg="red",fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"), width=24, state="readonly")
        combo_Search["value"]=("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial", 13, "bold"),width=24)
        txtSearch.grid(row=0, column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        # ===============Show Data Table=============
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-In")

        self.room_table.heading("checkout", text="Check-Out")
        self.room_table.heading("roomtype", text="Room Type")

        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="No Of Days")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column ("checkin", width=100)
        self.room_table.column ("checkout",width=100)
        self.room_table.column ("roomtype", width=100)
        self.room_table.column ("roomavailable", width=100)
        self.room_table.column ("meal", width=100)
        self.room_table.column ("noOfdays", width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor )
        self.fetch_data()

        #====add data=====
    def add_data(self):
        if self.var_contact.get()==""or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO room VALUES (%s, %s, %s, %s, %s, %s,%s)",(
                                                                                            self.var_contact.get(),
                                                                                            self.var_checkin.get(),
                                                                                            self.var_checkout.get(),
                                                                                            self.var_roomtype.get(),
                                                                                            self.var_roomavailable.get(),
                                                                                            self.var_meal.get(),
                                                                                            self.var_noOfdays.get()
                                                                                            
                                                                                            )) 
                conn.commit()
                self.fetch_data()
                conn.close()  
                messagebox.showinfo("success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)  

    #=======fetch data========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=======get cursor=======
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noOfdays.set(row[6]),
    
    #======update function======
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,meal=%s,noOfdays=%s where contact=%s",(
                                                                                                                                        self.var_checkin.get(),
                                                                                                                                        self.var_checkout.get(),
                                                                                                                                        self.var_roomtype.get(),
                                                                                                                                        self.var_meal.get(),
                                                                                                                                        self.var_noOfdays.get(),
                                                                                                                                        self.var_contact.get()
                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

    #==========delete function=======
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            messagebox.showinfo("Success","Customer has been deleted")
            conn.commit() 
        self.fetch_data() 
        conn.close()        

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        # self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noOfdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set(""),
    
    
    #===========All Data Fetch==============
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root) 
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
            my_cursor=conn.cursor()       
            query=("select Name from customer where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()  

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2) 
                showDataframe.place(x=450,y=55,width=300,height=180) 

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                #===========gender===========

                conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
                my_cursor=conn.cursor()       
                query=("select Gender from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #===========email===========
                conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
                my_cursor=conn.cursor()       
                query=("select Email from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                #===========Nationality===========
                conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
                my_cursor=conn.cursor()       
                query=("select Nationality from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                #===========address===========
                conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
                my_cursor=conn.cursor()       
                query=("select Address from customer where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbladdress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lbladdress.place(x=0,y=120)

                lbl1=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl1.place(x=90,y=120)

    #====search system======
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
        my_cursor=conn.cursor()  

        my_cursor.execute("SELECT * FROM room WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()   

    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get() 
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noOfdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Launch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 

        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)        



if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()    