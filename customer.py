from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        self.var_ref=StringVar()
        self.var_cust_name=StringVar()
        self.var_DOB=StringVar()
        self.var_Address=StringVar()
        self.var_Mobile=StringVar()
        

        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)


        img2=Image.open(r"C:\Users\Harsh Singh\OneDrive\Pictures\Camera Roll\35181-NZV3DS.jpg")
        img2=img2.resize((100,140),Image.BILINEAR)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #label frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #Label and entry
        lbl_cust_ref=Label(labelframeleft,text="Cust_ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=Entry(labelframeleft, textvariable=self.var_ref, width=29,font=("times new roman",13,"bold"))
        enty_ref.grid(row=0,column=1)

        #Customer name

        cname=Label(labelframeleft,text="NAME",font=("times new roman",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=Entry(labelframeleft, textvariable=self.var_cust_name, width=29,font=("times new roman",13,"bold"))
        txtcname.grid(row=1,column=1)

        #DOB

        Dname=Label(labelframeleft,text="DOB",font=("times new roman",12,"bold"),padx=2,pady=6)
        Dname.grid(row=2,column=0,sticky=W)

        txtDname=Entry(labelframeleft,textvariable=self.var_DOB, width=29,font=("times new roman",13,"bold"))
        txtDname.grid(row=2,column=1)

        #Address

        lblAddress=Label(labelframeleft,text="ADDRESS",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=3,column=0,sticky=W)

        txtAddress=Entry(labelframeleft,textvariable=self.var_Address, width=29,font=("times new roman",13,"bold"))
        txtAddress.grid(row=3,column=1)

        #Mobile_no

        lblMobile=Label(labelframeleft,text="MOBILE_NO",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=4,column=0,sticky=W)

        txtMobile=ttk.Entry(labelframeleft, textvariable=self.var_Mobile, width=29,font=("times new roman",13,"bold"))
        txtMobile.grid(row=4,column=1)

        #Button
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add", command=self.add_data, font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mdelete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #Table frame
        
        Tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"),padx=2)
        Tableframe.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Tableframe,text="Search By:",bg="red",fg="white",font=("times new roman",12,"bold"))
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Tableframe,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("MOBILE_NO","Cust_ID")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Tableframe,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)


        btnSearch=Button(Tableframe,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Tableframe,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #Show data table

        details_table=Frame(Tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ID","NAME","DOB","ADDRESS","MOBILE_NO"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("#1", text="ID")
        self.Cust_Details_Table.heading("#2", text="NAME")
        self.Cust_Details_Table.heading("#3", text="DOB")
        self.Cust_Details_Table.heading("#4", text="ADDRESS")
        self.Cust_Details_Table.heading("#5", text="MOBILE_NO")


        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ID",width=100)
        self.Cust_Details_Table.column("NAME",width=100)
        self.Cust_Details_Table.column("DOB",width=100)
        self.Cust_Details_Table.column("ADDRESS",width=100)
        self.Cust_Details_Table.column("MOBILE_NO",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_Mobile.get()=="" or self.var_cust_name.get()=="":
            messagebox.showerror("Error","All Fields are required", parent = self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s, %s, %s, %s, %s)",(self.var_ref.get(),
                                                                                    self.var_cust_name.get(),
                                                                                    self.var_DOB.get(),
                                                                                    self.var_Address.get(),
                                                                                    self.var_Mobile.get()
                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}", parent = self.root)
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
           self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
           for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
        conn.close()

    def get_cuersor(self, events=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_DOB.set(row[2]),
        self.var_Address.set(row[3]),
        self.var_Mobile.set(row[4]),
        


    def update(self):
        if self.var_Mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
    


        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,DOB=%s,ADDRESS=%s,MOBILE_NO=%s where CUST_ID=%s",(
                                                                                        
                                                                                                self.var_cust_name.get(),
                                                                                                self.var_DOB.get(),
                                                                                                self.var_Address.get(),
                                                                                                self.var_Mobile.get(),
                                                                                                self.var_ref.get()

                                                                                            ))

                                                                                                  
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated succesfully",parent=self.root )                                                                     
    
    #Delete

    def mdelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
            my_cursor=conn.cursor()
            query="Delete from customer where CUST_ID=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_DOB.set(""),
        self.var_Address.set(""),
        self.var_Mobile.set("")

    def search(self):
            
            
    
            conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
            my_cursor = conn.cursor()

            # Corrected line of code
            my_cursor.execute("SELECT * FROM customer WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")

            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                    self.Cust_Details_Table.insert("", END, values=i)
                    conn.commit()
            conn.close()
        
            

   

if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()