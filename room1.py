from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image, ImageTk

class Room_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System - Room Details")
        self.root.geometry("1295x550+230+220")

        self.var_hotel_id = StringVar()
        self.var_cust_id = StringVar()
        self.var_room_no = StringVar()
        self.var_room_type = StringVar()

        img2 = Image.open(r"C:\Users\Harsh Singh\OneDrive\Pictures\Camera Roll\35181-NZV3DS.jpg")  # Update the path accordingly
        img2 = img2.resize((100, 140), Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_title = Label(self.root, text="ADD ROOM DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Details", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # Hotel ID
        lbl_hotel_id = Label(labelframeleft, text="Hotel ID", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_hotel_id.grid(row=0, column=0, sticky=W)

        enty_hotel_id = Entry(labelframeleft, textvariable=self.var_hotel_id, width=29, font=("times new roman", 13, "bold"))
        enty_hotel_id.grid(row=0, column=1)

        # Customer ID
        lbl_cust_id = Label(labelframeleft, text="Customer ID", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_id.grid(row=1, column=0, sticky=W)

        enty_cust_id = Entry(labelframeleft, textvariable=self.var_cust_id, width=29, font=("times new roman", 13, "bold"))
        enty_cust_id.grid(row=1, column=1)

        # Room No
        lbl_room_no = Label(labelframeleft, text="Room No", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_room_no.grid(row=2, column=0, sticky=W)

        enty_room_no = Entry(labelframeleft, textvariable=self.var_room_no, width=29, font=("times new roman", 13, "bold"))
        enty_room_no.grid(row=2, column=1)

        # Room Type
        lbl_room_type = Label(labelframeleft, text="Room Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_room_type.grid(row=3, column=0, sticky=W)

        enty_room_type = ttk.Combobox(labelframeleft, textvariable=self.var_room_type, width=29, font=("times new roman", 13, "bold"), state="readonly")
        enty_room_type["value"] = ("Classic", "Delux")
        enty_room_type.current(0)
        enty_room_type.grid(row=3, column=1)

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
        combo_Search["value"] = ("cust_id", "room_no")  # Update the values accordingly
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Tableframe, textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Tableframe, text="Search", command=self.search, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Tableframe, text="Show All", command=self.fetch_data, font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # Show data table
        details_table = Frame(Tableframe, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Room_Details_Table = ttk.Treeview(details_table, column=("Hotel ID", "Customer ID", "Room No", "Room Type"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Room_Details_Table.xview)
        scroll_y.config(command=self.Room_Details_Table.yview)

        self.Room_Details_Table.heading("#1", text="Hotel ID")
        self.Room_Details_Table.heading("#2", text="Customer ID")
        self.Room_Details_Table.heading("#3", text="Room No")
        self.Room_Details_Table.heading("#4", text="Room Type")

        self.Room_Details_Table["show"] = "headings"

        self.Room_Details_Table.column("Hotel ID", width=100)
        self.Room_Details_Table.column("Customer ID", width=100)
        self.Room_Details_Table.column("Room No", width=100)
        self.Room_Details_Table.column("Room Type", width=100)

        self.Room_Details_Table.pack(fill=BOTH, expand=1)
        self.Room_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_hotel_id.get() == "" or self.var_cust_id.get() == "" or self.var_room_no.get() == "" or self.var_room_type.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room (hotel_id, cust_id, room_no, room_type) values(%s, %s, %s, %s)", (self.var_hotel_id.get(),
                                                                                                                       self.var_cust_id.get(),
                                                                                                                       self.var_room_no.get(),
                                                                                                                       self.var_room_type.get()
                                                                                                                       ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room details have been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM room")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.Room_Details_Table.delete(*self.Room_Details_Table.get_children())
                for i in rows:
                    self.Room_Details_Table.insert("", END, values=i)
            conn.commit()
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
        finally:
            conn.close()

    def get_cursor(self, events=""):
        cursor_row = self.Room_Details_Table.focus()
        content = self.Room_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_hotel_id.set(row[0])
        self.var_cust_id.set(row[1])
        self.var_room_no.set(row[2])
        self.var_room_type.set(row[3])

    def update(self):
        if self.var_hotel_id.get() == "":
            messagebox.showerror("Error", "Please enter hotel ID", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set cust_id=%s, room_no=%s, room_type=%s where hotel_id=%s", (
                self.var_cust_id.get(),
                self.var_room_no.get(),
                self.var_room_type.get(),
                self.var_hotel_id.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details have been updated successfully", parent=self.root)

    def mdelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this room", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
            my_cursor = conn.cursor()
            query = "Delete from room where hotel_id=%s"
            value = (self.var_hotel_id.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_hotel_id.set("")
        self.var_cust_id.set("")
        self.var_room_no.set("")
        self.var_room_type.set("")

    def search(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="harsh8172", database="hotel_system")
            my_cursor = conn.cursor()

            my_cursor.execute(f"SELECT * FROM room WHERE {self.search_var.get()} LIKE '%{self.txt_search.get()}%'")

            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.Room_Details_Table.delete(*self.Room_Details_Table.get_children())
                for i in rows:
                    self.Room_Details_Table.insert("", END, values=i)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
        finally:
            conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Room_Win(root)
    root.mainloop()
