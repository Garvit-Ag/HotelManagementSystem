from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class Payment_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System - Payment Details")
        self.root.geometry("1295x550+230+220")

        self.var_payment_no = StringVar()
        self.var_payment_amt = StringVar()
        self.var_payment_date = StringVar()
        self.var_payment_method = StringVar()

        lbl_title = Label(self.root, text="PAYMENT DETAILS", font=("times new roman", 18, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Payment Details",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # Label and entry
        lbl_payment_no = Label(labelframeleft, text="Payment_No", font=("times new roman", 12, "bold"),
                               padx=2, pady=6)
        lbl_payment_no.grid(row=0, column=0, sticky=W)

        enty_payment_no = Entry(labelframeleft, textvariable=self.var_payment_no, width=29,
                                font=("times new roman", 13, "bold"))
        enty_payment_no.grid(row=0, column=1)

        lbl_payment_amt = Label(labelframeleft, text="Payment_amt", font=("times new roman", 12, "bold"),
                                padx=2, pady=6)
        lbl_payment_amt.grid(row=1, column=0, sticky=W)

        enty_payment_amt = Entry(labelframeleft, textvariable=self.var_payment_amt, width=29,
                                 font=("times new roman", 13, "bold"))
        enty_payment_amt.grid(row=1, column=1)

        lbl_payment_date = Label(labelframeleft, text="Payment_Date", font=("times new roman", 12, "bold"),
                                 padx=2, pady=6)
        lbl_payment_date.grid(row=2, column=0, sticky=W)

        enty_payment_date = Entry(labelframeleft, textvariable=self.var_payment_date, width=29,
                                  font=("times new roman", 13, "bold"))
        enty_payment_date.grid(row=2, column=1)

        lbl_payment_method = Label(labelframeleft, text="Payment_meth", font=("times new roman", 12, "bold"),
                                   padx=2, pady=6)
        lbl_payment_method.grid(row=3, column=0, sticky=W)

        self.payment_method_combo = ttk.Combobox(labelframeleft, textvariable=self.var_payment_method,
                                                 font=("times new roman", 12, "bold"), width=27, state="readonly")
        self.payment_method_combo["values"] = ("Online", "Cash")
        self.payment_method_combo.current(0)
        self.payment_method_combo.grid(row=3, column=1)

        # Button
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=430, width=412, height=50)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 11, "bold"),
                        bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=5)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 11, "bold"),
                           bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=5)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete, font=("arial", 11, "bold"),
                           bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=5)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 11, "bold"),
                          bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=5)

        # Table frame
        Tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="Payment Details",
                                font=("times new roman", 12, "bold"), padx=2)
        Tableframe.place(x=435, y=50, width=860, height=490)

        details_table = Frame(Tableframe, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        lblSearchBy=Label(Tableframe,text="Search By:",bg="red",fg="white",font=("times new roman",12,"bold"))
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Tableframe,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Payment_No")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Tableframe,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Tableframe,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Tableframe,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Payment_Details_Table = ttk.Treeview(details_table,
                                                   column=("Payment_No", "Payment_amt", "Payment_Date", "Payment_meth"),
                                                   xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Payment_Details_Table.xview)
        scroll_y.config(command=self.Payment_Details_Table.yview)

        self.Payment_Details_Table.heading("#1", text="Payment_No")
        self.Payment_Details_Table.heading("#2", text="Payment_amt")
        self.Payment_Details_Table.heading("#3", text="Payment_Date")
        self.Payment_Details_Table.heading("#4", text="Payment_meth")

        self.Payment_Details_Table["show"] = "headings"

        self.Payment_Details_Table.column("Payment_No", width=100)
        self.Payment_Details_Table.column("Payment_amt", width=100)
        self.Payment_Details_Table.column("Payment_Date", width=100)
        self.Payment_Details_Table.column("Payment_meth", width=100)

        self.Payment_Details_Table.pack(fill=BOTH, expand=1)
        self.Payment_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_payment_no.get() == "" or self.var_payment_amt.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172",
                                               database="hotel_system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into payment values(%s, %s, %s, %s)",
                                  (self.var_payment_no.get(),
                                   self.var_payment_amt.get(),
                                   self.var_payment_date.get(),
                                   self.var_payment_method.get()
                                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Payment details have been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172",
                                       database="hotel_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from payment")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Payment_Details_Table.delete(*self.Payment_Details_Table.get_children())
            for i in rows:
                self.Payment_Details_Table.insert("", END, values=i)
                conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Payment_Details_Table.focus()
        content = self.Payment_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_payment_no.set(row[0])
        self.var_payment_amt.set(row[1])
        self.var_payment_date.set(row[2])
        self.var_payment_method.set(row[3])

    def update(self):
        if self.var_payment_no.get() == "":
            messagebox.showerror("Error", "Please select a payment to update", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172",
                                               database="hotel_system")
                my_cursor = conn.cursor()
                print("Updating Payment")
                print(f"Payment_No: {self.var_payment_no.get()}")
                print(f"Payment_amt: {self.var_payment_amt.get()}")
                print(f"Payment_Date: {self.var_payment_date.get()}")
                print(f"Payment_meth: {self.var_payment_method.get()}")
                my_cursor.execute("update payment set Payment_amt=%s, Payment_Date=%s, Payment_meth=%s where Payment_No=%s",
                                  (self.var_payment_amt.get(),
                                   self.var_payment_date.get(),
                                   self.var_payment_method.get(),
                                   self.var_payment_no.get()
                                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "Payment details have been updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def delete(self):
        if self.var_payment_no.get() == "":
            messagebox.showerror("Error", "Please select a payment to delete", parent=self.root)
        else:
            mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this payment?",
                                           parent=self.root)
            if mDelete > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172",
                                               database="hotel_system")
                my_cursor = conn.cursor()
                query = "Delete from payment where Payment_no=%s"
                value = (self.var_payment_no.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                self.fetch_data()
                conn.close()

    def reset(self):
        self.var_payment_no.set("")
        self.var_payment_amt.set("")
        self.var_payment_date.set("")
        self.var_payment_method.set("")

    def search(self):
        if self.search_var.get() == "":
            messagebox.showerror("Error", "Please select a field to search", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172",
                                       database="hotel_system")
            my_cursor = conn.cursor()
            my_cursor.execute(f"select * from payment where {self.search_var.get()}=%s", (self.txt_search.get(),))
            rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Payment_Details_Table.delete(*self.Payment_Details_Table.get_children())
            for i in rows:
                self.Payment_Details_Table.insert("", END, values=i)
                conn.commit()
        else:
            messagebox.showinfo("Info", "No record found", parent=self.root)
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Payment_Win(root)
    root.mainloop()
