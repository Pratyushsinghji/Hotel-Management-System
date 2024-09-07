from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x500+180+70")


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
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        # Floor
        Ibl_floor=Label(labelframeleft,text="Floor",font=("times new roman",12,"bold"),padx=2,pady=6)
        Ibl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,width=20,textvariable=self.var_floor,font=("times new roman",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        # Room No
        Ibl_RoomNo=Label(labelframeleft,text="Room No:",font=("times new roman",12,"bold"),padx=2,pady=6)
        Ibl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,width=20,textvariable=self.var_roomNo,font=("times new roman",13,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        # RoomType
        Ibl_RoomType=Label(labelframeleft,text="Room Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        Ibl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(labelframeleft,width=20,textvariable=self.var_RoomType ,font=("times new roman",13,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)

        # ===============btns===============
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnUpdate .grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial", 11, "bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        # ===============tabel frame search system=============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=600,y=55,width=600,height=350)


        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,columns=("floor","roomno","roomType",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomType", text="Room Type")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column ("roomno", width=100)
        self.room_table.column ("roomType", width=100)
    
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor )
        self.fetch_data()

    #====add data=====
    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO details VALUES (%s, %s, %s)", (
                                                                            self.var_floor.get(),
                                                                            self.var_roomNo.get(),
                                                                            self.var_RoomType.get()
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New Room Added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    #=======fetch data========
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2]),

    #======update function======
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Floor number",parent=self.root)
        else:    
            conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                        self.var_floor.get(),
                                                                                        self.var_RoomType.get(),
                                                                                        self.var_roomNo.get()
                                                                                    ))
            conn.commit()
            self.fetch_data() 
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

    #==========delete function=======
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want delete this Room Details",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="pratyush@123",database="hotel management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit() 
        self.fetch_data() 
        conn.close()  

    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set(""),


if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()            