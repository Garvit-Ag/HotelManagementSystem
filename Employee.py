from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image, ImageTk

class Emp_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System - Employee Details")
        self.root.geometry("1295x550+230+220")

        self.var_emp_id = StringVar()
        self.var_emp_name = StringVar()
        self.var_job_desc = StringVar()
        self.var_emp_address = StringVar()
        self.var_emp_mobile = StringVar()


        lbl_title = Label(self.root, text="ADD EMPLOYEE DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Employee Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # Employee ID
        lbl_emp_id = Label(labelframeleft, text="Employee ID", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_emp_id.grid(row=0, column=0, sticky=W)

        enty_emp_id = Entry(labelframeleft, textvariable=self.var_emp_id, width=29, font=("times new roman", 13, "bold"))
        enty_emp_id.grid(row=0, column=1)

        # Employee Name
        lbl_emp_name = Label(labelframeleft, text="Employee Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_emp_name.grid(row=1, column=0, sticky=W)

        enty_emp_name = Entry(labelframeleft, textvariable=self.var_emp_name, width=29, font=("times new roman", 13, "bold"))
        enty_emp_name.grid(row=1, column=1)

        # Job Description
        lbl_job_desc = Label(labelframeleft, text="Job Description", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_job_desc.grid(row=2, column=0, sticky=W)

        enty_job_desc = Entry(labelframeleft, textvariable=self.var_job_desc, width=29, font=("times new roman", 13, "bold"))
        enty_job_desc.grid(row=2, column=1)

        # Employee Address
        lbl_emp_address = Label(labelframeleft, text="Employee Address", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_emp_address.grid(row=3, column=0, sticky=W)

        enty_emp_address = Entry(labelframeleft, textvariable=self.var_emp_address, width=29, font=("times new roman", 13, "bold"))
        enty_emp_address.grid(row=3, column=1)

        # Employee Mobile No
        lbl_emp_mobile = Label(labelframeleft, text="Mobile No", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_emp_mobile.grid(row=4, column=0, sticky=W)

        enty_emp_mobile = Entry(labelframeleft, textvariable=self.var_emp_mobile, width=29, font=("times new roman", 13, "bold"))
        enty_emp_mobile.grid(row=4, column=1)

        # Button
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mdelete, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # Table frame
        Tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("times new roman", 12, "bold"), padx=2)
        Tableframe.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Tableframe, text="Search By:", bg="red", fg="white", font=("times new roman", 12, "bold"))
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Tableframe, textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_Search["value"] = ("Mobile_No", "Emp_ID")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Tableframe, textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Tableframe, text="Search", command=self.search, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Tableframe, text="Show All", command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # Table Frame
        details_table = Frame(Tableframe, bd=2, relief=RIDGE)
        details_table.place(x=10, y=50, width=835, height=430)

        scroll_x = Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = Scrollbar(details_table, orient=VERTICAL)

        self.emp_details_table = ttk.Treeview(details_table, columns=(
            "Employee ID", "Employee Name", "Job Description", "Address", "Mobile No"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.emp_details_table.xview)
        scroll_y.config(command=self.emp_details_table.yview)

        self.emp_details_table.heading("Employee ID", text="Employee ID")
        self.emp_details_table.heading("Employee Name", text="Employee Name")
        self.emp_details_table.heading("Job Description", text="Job Description")
        self.emp_details_table.heading("Address", text="Address")
        self.emp_details_table.heading("Mobile No", text="Mobile No")

        self.emp_details_table["show"] = "headings"
        self.emp_details_table.column("Employee ID", width=100)
        self.emp_details_table.column("Employee Name", width=100)
        self.emp_details_table.column("Job Description", width=100)
        self.emp_details_table.column("Address", width=100)
        self.emp_details_table.column("Mobile No", width=100)

        self.emp_details_table.pack(fill=BOTH, expand=1)
        self.emp_details_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def add_data(self):
        if self.var_emp_id.get() == "" or self.var_emp_name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO employee (Emp_id, Emp_Name, Job_Descrp, Address, Mobile_No) VALUES (%s, %s, %s, %s, %s)", (
                    self.var_emp_id.get(),
                    self.var_emp_name.get(),
                    self.var_job_desc.get(),
                    self.var_emp_address.get(),
                    self.var_emp_mobile.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Employee details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM employee")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.emp_details_table.delete(*self.emp_details_table.get_children())
            for row in rows:
                self.emp_details_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.emp_details_table.focus()
        contents = self.emp_details_table.item(cursor_row)
        row = contents["values"]
        self.var_emp_id.set(row[0])
        self.var_emp_name.set(row[1])
        self.var_job_desc.set(row[2])
        self.var_emp_address.set(row[3])
        self.var_emp_mobile.set(row[4])

    def update(self):
        if self.var_emp_id.get() == "":
            messagebox.showerror("Error", "Please select a record to update", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE employee SET Emp_Name=%s, Job_Descrp=%s, Address=%s, Mobile_No=%s WHERE Emp_id=%s", (
                    self.var_emp_name.get(),
                    self.var_job_desc.get(),
                    self.var_emp_address.get(),
                    self.var_emp_mobile.get(),
                    self.var_emp_id.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "Employee details have been updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def mdelete(self):
        if self.var_emp_id.get() == "":
            messagebox.showerror("Error", "Please select a record to delete", parent=self.root)
        else:
            mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this employee", parent=self.root)
            if mDelete:
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
                    my_cursor = conn.cursor()
                    query = "DELETE FROM employee WHERE Emp_id=%s"
                    value = (self.var_emp_id.get(),)
                    my_cursor.execute(query, value)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete", "Employee details have been deleted successfully", parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def reset(self):
        self.var_emp_id.set("")
        self.var_emp_name.set("")
        self.var_job_desc.set("")
        self.var_emp_address.set("")
        self.var_emp_mobile.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM employee WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.emp_details_table.delete(*self.emp_details_table.get_children())
            for row in rows:
                self.emp_details_table.insert("", END, values=row)
            conn.commit()
        conn.close()

        
if __name__=="__main__":
    root = Tk()
    obj = Emp_Win(root)
    root.mainloop()
