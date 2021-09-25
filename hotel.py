from tkinter import  *
from PIL import  Image,ImageTk
from customer import  CustomerWin
class  HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry("1550x800")

        # ============================== Fist Image =========================

        image1 = Image.open('/home/kawsar/Software/image/hotel.jpg')
        image1 = image1.resize((1550,140),Image.ANTIALIAS)
        self.photoimage1  = ImageTk.PhotoImage(image1)
        lblimage = Label(self.root,image =self.photoimage1,bd=4,relief =RIDGE)
        lblimage.place(x=0,y=0,width=1550,height=140)

        # ============================== Logo Image =========================

        image2 = Image.open('/home/kawsar/Software/image/logo.jpg')
        image2 = image2.resize((230,140),Image.ANTIALIAS)
        self.photoimage2  = ImageTk.PhotoImage(image2)
        lblimage = Label(self.root,image =self.photoimage2,bd=4,relief =RIDGE)
        lblimage.place(x=0,y=0,width=230,height=140)


        # ============================== Tile =========================
        lbl_title = Label(self.root,text="Hotel Management System",font= ('times new roman',40,'bold'),bg='black',fg='gold',bd =4 ,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        # ============================== main Frame =========================
        main_frame = Frame(self.root,bd=4,relief =RIDGE)
        main_frame.place(x=0,y=190,width=1550,height =620)


        # ============================== Menu =========================
        lbl_menu = Label(main_frame , text="Menu",font= ('times new roman',20,'bold'),bg='black',fg='gold',bd =4 ,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)


        # ============================== Button Frame =========================
        button_frame = Frame(main_frame,bd=4,relief =RIDGE)
        button_frame.place(x=0,y=35,width=228,height =190)
        # ================================ customer button ================================
        customer_button  =Button(button_frame,text = 'CUSTOMER', command = self.customer_details, width=22,font= ('times new roman',14,'bold'),bg='black',fg='gold',bd =0,cursor='hand1')
        customer_button.grid(row=0,column=0)

        # ================================ room button ================================
        room_button  =Button(button_frame,text = 'ROOM',width=22,font= ('times new roman',14,'bold'),bg='black',fg='gold',bd =0,cursor='hand1')
        room_button.grid(row=1,column=0)

        # ================================ details button ================================
        details_button  =Button(button_frame,text = 'DETAILS',width=22,font= ('times new roman',14,'bold'),bg='black',fg='gold',bd =0,cursor='hand1')
        details_button.grid(row=2,column=0)

        # ================================ report button ================================
        report_button  =Button(button_frame,text = 'REPORT',width=22,font= ('times new roman',14,'bold'),bg='black',fg='gold',bd =0,cursor='hand1')
        report_button.grid(row=3,column=0)

        # ================================ logout button ================================
        logout_button  =Button(button_frame,text = 'LOGOUT',width=22,font= ('times new roman',14,'bold'),bg='black',fg='gold',bd =0,cursor='hand1')
        logout_button.grid(row=4,column=0)



        # ============================== Image 3 =========================

        image3 = Image.open('/home/kawsar/Software/image/image1.jpg')
        image3 = image3.resize((1310,590),Image.ANTIALIAS)
        self.photoimage3  = ImageTk.PhotoImage(image3)
        lblimage = Label(main_frame,image =self.photoimage3,bd=4,relief =RIDGE)
        lblimage.place(x=225,y=0,width=1310,height=590)





        # ============================== Down Image 1 =========================

        image4 = Image.open('/home/kawsar/Software/image/image2.jpg')
        image4 = image4.resize((230,210),Image.ANTIALIAS)
        self.photoimage4  = ImageTk.PhotoImage(image4)
        lblimage = Label(main_frame,image =self.photoimage4,bd=4,relief =RIDGE)
        lblimage.place(x=0,y=225,width=230,height=210)




        # ============================== Down Image 2 =========================

        image5 = Image.open('/home/kawsar/Software/image/image3.jpeg')
        image5 = image5.resize((230,190),Image.ANTIALIAS)
        self.photoimage5  = ImageTk.PhotoImage(image5)
        lblimage = Label(main_frame,image =self.photoimage5,bd=4,relief =RIDGE)
        lblimage.place(x=0,y=420,width=230,height=190)


    def customer_details(self):
        self.new_window = Toplevel(self.root)
        self.app = CustomerWin(self.new_window)











if __name__ == '__main__':
    root=Tk()
    obj =HotelManagementSystem(root)
    root.mainloop()





