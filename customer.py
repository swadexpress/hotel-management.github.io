from tkinter import  *
from PIL import  Image,ImageTk
from tkinter import ttk
import mysql.connector 
import  random
from tkinter import  messagebox 

class  CustomerWin:
    def __init__(self,root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry("1295x550")


        # ============================== Variables =========================
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(x)
        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_ = StringVar()
        self.var_id_number = StringVar()


        # ============================== Tile =========================
        lbl_title = Label(self.root,text="ADD CUSTOMER DETAILS",font= ('times new roman',18,'bold'),bg='black',fg='gold',bd =4 ,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        # ============================== Logo Image =========================

        image2 = Image.open('/home/kawsar/Software/image/logo.jpg')
        image2 = image2.resize((100,40),Image.ANTIALIAS)
        self.photoimage2  = ImageTk.PhotoImage(image2)
        lblimage = Label(self.root,image =self.photoimage2,bd=0,relief =RIDGE)
        lblimage.place(x=0,y=0,width=100,height=45)


        # ============================== label frame left =========================

        labelframeleft = LabelFrame(self.root,bd=2,relief =RIDGE,text='Cusomer Details ',font= ('times new roman',12,'bold'),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        # ============================== Cusomer Ref No =========================

        label_ref= Label(labelframeleft,text='Ref No ',font= ('times new roman',12,'bold'),padx=2,pady=6)
        label_ref.grid(row=0,column=0,sticky= W)
        entry_ref= ttk.Entry(labelframeleft,width=22,textvariable = self.var_ref ,state ='readonly' ,font= ('times new roman',12,'bold'))
        entry_ref.grid(row=0,column=1)



        # ============================== Cusomer  Name:  =========================

        label_customer_name = Label(labelframeleft,text='Cusomer  Name: ',font= ('times new roman',12,'bold'),padx=2,pady=6)
        label_customer_name.grid(row=1,column=0,sticky= W)
        entry_mother_name = ttk.Entry(labelframeleft,width=22,  textvariable = self.var_cust_name , font= ('times new roman',12,'bold'))
        entry_mother_name.grid(row=1,column=1)




        # ============================== Cusomer Mother Name:  =========================

        label_customer_mother_name = Label(labelframeleft,text='Cusomer Mother Name: ',font= ('times new roman',12,'bold'),padx=2,pady=6)
        label_customer_mother_name.grid(row=2,column=0,sticky= W)
        entry_mother_name = ttk.Entry(labelframeleft,width=22,  textvariable = self.var_mother , font= ('times new roman',12,'bold'))
        entry_mother_name.grid(row=2,column=1)



        # ============================== gender  =========================

        label_customer_gender= Label(labelframeleft,text='Cusomer gender: ',font= ('times new roman',12,'bold'),padx=2,pady=6)
        label_customer_gender.grid(row=3,column=0,sticky= W)
        combo_gender = ttk.Combobox(labelframeleft,textvariable = self.var_gender,font= ('times new roman',12,'bold'),width=21,state ='readonly')
        combo_gender['value']= ('Male','Female','Other')
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


        # ============================== Cusomer Post Code  =========================

        label_customer_postcode = Label(labelframeleft,text='Cusomer Post Code: ',font= ('times new roman',12,'bold'),padx=2,pady=6)
        label_customer_postcode.grid(row=4,column=0,sticky= W)
        entry_postcode = ttk.Entry(labelframeleft,width=22,textvariable = self.var_post ,font= ('times new roman',12,'bold'))
        entry_postcode.grid(row=4,column=1)




        # ============================== Cusomer Phone Number  =========================

        label_customer_phone_number = Label(labelframeleft,text='Cusomer Phone Number: ',font= ('times new roman',12,'bold'),padx=2,pady=6)
        label_customer_phone_number.grid(row=5,column=0,sticky= W)
        entry_phone_number = ttk.Entry(labelframeleft,width=22  ,textvariable = self.var_mobile ,font= ('times new roman',12,'bold'))
        entry_phone_number.grid(row=5,column=1)




        # ============================== Cusomer email  =========================

        label_customer_email = Label(labelframeleft,text='Cusomer Email: ',font= ('times new roman',12,'bold'),padx=2,pady=6)
        label_customer_email.grid(row=6,column=0,sticky= W)
        entry_email = ttk.Entry(labelframeleft,width=22 ,textvariable = self.var_email ,font= ('times new roman',12,'bold'))
        entry_email.grid(row=6,column=1)



        # ============================== Cusomer Nationality  =========================

        label_customer_nationality  = Label(labelframeleft,text='Cusomer Nationality: ',font= ('times new roman',12,'bold'),padx=2,pady=6)
        label_customer_nationality .grid(row=7,column=0,sticky= W)
        combo_nationality  = ttk.Combobox(labelframeleft,font= ('times new roman',12,'bold'),width=21 ,textvariable = self.var_nationality,state ='readonly')
        combo_nationality ['value']= ('Bangladesh','Indian','Pakistan')
        combo_nationality.current(0) 
        combo_nationality.grid(row=7,column=1)





        # ============================== Cusomer IDProof type =========================


        label_customer_id_proof= Label(labelframeleft,text='ID Proof',font= ('times new roman',12,'bold'),padx=2,pady=6)
        label_customer_id_proof.grid(row=8,column=0,sticky= W)
        combo_id_proof = ttk.Combobox(labelframeleft,font= ('times new roman',12,'bold'),width=21 ,textvariable = self.var_id_proof  ,state ='readonly')
        combo_id_proof['value']= ('NID','Passport','DrivingLicence')
        combo_id_proof.current(0) 
        combo_id_proof.grid(row=8,column=1)



        # ============================== Cusomer NID Card  =========================

        label_customer_nid_card= Label(labelframeleft,text='Cusomer NID Card NO : ',font= ('times new roman',12,'bold'),padx=2,pady=6)
        label_customer_nid_card.grid(row=9,column=0,sticky= W)
        entry_nid_card= ttk.Entry(labelframeleft,width=22 ,textvariable = self.var_id_number ,font= ('times new roman',12,'bold'))
        entry_nid_card.grid(row=9,column=1)


        # ============================== Cusomer Address =========================

        label_customer_address= Label(labelframeleft,text='Cusomer Address : ',font= ('times new roman',12,'bold'),padx=2,pady=6)
        label_customer_address.grid(row=10,column=0,sticky= W)
        entry_address= ttk.Entry(labelframeleft,width=22 ,textvariable = self.var_address ,font= ('times new roman',12,'bold'))
        entry_address.grid(row=10,column=1)


        # ============================== Buttons =========================
        button_frame= Frame(labelframeleft,bd=2,relief =RIDGE)
        button_frame.place(x=0,y=400,width=410,height=40)

        # ============================== Add Button =========================
        add_button = Button(button_frame,command=self.add_data,text='Add',font =('arial',12,'bold'),bg='black',fg='gold',width=8)
        add_button.grid(row=0,column=0,padx=1,pady=2)

        # ============================== Update Button =========================
        update_button = Button(button_frame,text='Update', command =self.update,font =('arial',12,'bold'),bg='black',fg='gold',width=8)
        update_button.grid(row=0,column=1,padx=1,pady=2)

        # ============================== Delete Button =========================
        delete_button = Button(button_frame,text='Delete',font =('arial',12,'bold'),bg='black',fg='gold',width=8)
        delete_button.grid(row=0,column=2,padx=1,pady=2)

        # ============================== Reset Button =========================
        reset_button = Button(button_frame,text='Reset',font =('arial',12,'bold'),bg='black',fg='gold',width=8)
        reset_button.grid(row=0,column=3,padx=1,pady=2)


        # ================================= Table Frame===============================

        table_frame = LabelFrame(self.root,bd=2,relief =RIDGE,text='View Details and Searche System ',font= ('times new roman',12,'bold'),padx=2)
        table_frame.place(x=435,y=50,width=860,height=490)



        # ============================== Searching Text Input  =========================

        label_search_by= Label(table_frame,text='Search By: ',font= ('times new roman',12,'bold'),bg='red',fg='white')
        label_search_by.grid(row=0,column=0,sticky= W,padx=2)
        self.search_var = StringVar()


        combo_search= ttk.Combobox(table_frame,font= ('times new roman',12,'bold'),width=15,state ='readonly')
        combo_search['value']= ('Mobile','Ref')
        combo_search.current(0) 
        combo_search.grid(row=0,column=1,padx=2)
        self.text_search = StringVar()
        text_search= ttk.Entry(table_frame,width=26,font= ('times new roman',12,'bold'))
        text_search.grid(row=0,column=2)


       # ============================== Search Button =========================
        search_button = Button(table_frame,text='Search',font =('arial',12,'bold'),bg='black',fg='gold',width=8)
        search_button.grid(row=0,column=3,padx=1,pady=2)

       # ============================== Show All Button =========================
        show_all_button = Button(table_frame,text='Show All',font =('arial',12,'bold'),bg='black',fg='gold',width=8)
        show_all_button.grid(row=0,column=4,padx=1,pady=2)



# ============================== Show Data Table =========================


        # ================================= Show Data Frame===============================

        details_table = LabelFrame(table_frame,bd=2,relief =RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x = ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table= ttk.Treeview(details_table,column =('ref','name',
            'mother','gender','post','mobile','email','nationality','idproof','idnumber',
            'address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)  

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        self.Cust_Details_Table.heading('ref',text='Ref No')
        self.Cust_Details_Table.heading('name',text='name')
        self.Cust_Details_Table.heading('mother',text='mother')
        self.Cust_Details_Table.heading('gender',text='gender')
        self.Cust_Details_Table.heading('post',text='post')
        self.Cust_Details_Table.heading('mobile',text='mobile')
        self.Cust_Details_Table.heading('nationality',text='nationality')
        self.Cust_Details_Table.heading('idproof',text='idproof')
        self.Cust_Details_Table.heading('idnumber',text='idnumber')
        self.Cust_Details_Table.heading('address',text='address')
        self.Cust_Details_Table['show']='headings'
        self.Cust_Details_Table.column('ref',width=100)
        self.Cust_Details_Table.column('name',width=100)
        self.Cust_Details_Table.column('mother',width=100)
        self.Cust_Details_Table.column('gender',width=100)
        self.Cust_Details_Table.column('post',width=100)
        self.Cust_Details_Table.column('mobile',width=100)
        self.Cust_Details_Table.column('nationality',width=100)
        self.Cust_Details_Table.column('idproof',width=100)
        self.Cust_Details_Table.column('idnumber',width=100)
        self.Cust_Details_Table.column('address',width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()






    def  add_data(self):
        if self.var_mobile.get() =='' or self.var_mother.get() == '':
            messagebox.showerror('Error','All  fields must be ',parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='',database='management')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo('Success','customer has been added',parent=self.root)
            except  Exception as es:
                print(es)
                messagebox.showwarning('Warning',f'Some thing went wrong : {str(es)}',parent=self.root)




    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='',database='management')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from customer')
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert('',END, values=i)

                conn.commit()
        conn.close()


    def  get_cuersor(self,event =""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row=content['values']

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]), 
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def  update(self):
        if self.var_mobile.get()=='':
            messagebox.showerror('Error','Plase add a number',parent=self.root)

        else:
            conn = mysql.connector.connect(host='localhost',username='root',password='',database='management')
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name =%s,Mother =%s,Genger =%s,PostCode =%s,Mobile =%s,Email =%s,Nationality =%s,Idproof =%s,Idnumber =%s,Address =%s, where  Reg =%s",(
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get(),
                    self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Upadata','Cusomer Detail has been update successfully')

                



# kawsarKhan12345


if __name__ == '__main__':
    root=Tk()
    obj =CustomerWin(root)
    root.mainloop()


