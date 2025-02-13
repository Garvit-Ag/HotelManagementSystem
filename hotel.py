from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room1 import Room_Win
from Employee import Emp_Win
from payment import Payment_Win


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x800+0+0")

        # Load and place images
        img1 = Image.open(r"C:\Users\Harsh Singh\OneDrive\Pictures\Camera Roll\pexels-thorsten-technoman-338504.jpg")
        img1 = img1.resize((1550, 140), Image.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        img2=Image.open(r"C:\Users\Harsh Singh\OneDrive\Pictures\Camera Roll\35181-NZV3DS.jpg")
        img2=img2.resize((230,140),Image.BILINEAR)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # Button frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        # Define the cust_details method within the HotelManagementSystem class
        def cust_details():
            new_window = Toplevel(self.root)
            app = Cust_Win(new_window)

        def roombooking():
            new_window = Toplevel(self.root)
            app = Room_Win(new_window)

        def emp_details():
            new_window = Toplevel(self.root)
            app = Emp_Win(new_window)

        def payment():
            new_window = Toplevel(self.root)
            app = Payment_Win(new_window)


        cust_btn = Button(btn_frame, text="CUSTOMER", command=cust_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM",command=roombooking, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="PAYMENT",command=payment, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="EMPLOYEE",command=emp_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        

        img3 = Image.open(r"C:\Users\Harsh Singh\OneDrive\Pictures\Camera Roll\hotel.jpg")
        img3 = img3.resize((1310, 590), Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)

        # Down images
        img4 = Image.open(r"C:\Users\Harsh Singh\OneDrive\Pictures\Camera Roll\rktkn-ssOtyGE8CyE-unsplash.jpg")
        img4 = img4.resize((230, 210), Image.BILINEAR)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg2 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"C:\Users\Harsh Singh\OneDrive\Pictures\Camera Roll\food-4507705_1280.jpg")
        img5 = img5.resize((230, 190), Image.BILINEAR)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg3 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg3.place(x=0, y=420, width=230, height=190)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
