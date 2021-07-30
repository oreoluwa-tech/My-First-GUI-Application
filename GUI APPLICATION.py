from tkinter import*
import sqlite3

root = Tk()
root.title('Honeycomb Cakes Customer Information System!')
root.geometry('550x420')
root.iconbitmap(r"C:\Users\Oreoluwa Daramola\Documents\Data Science projects\cake.ico")
root.configure(bg='black')

#Create Data base

con = sqlite3.connect('Customer Information.db')
cursor = con.cursor()
#Create Table

#cursor.execute("""CREATE TABLE Customers (id integer PRIMARY KEY,full_name text,home_adress text,phone text,email text,items_ordered text,amount_paid real,delivery_address text))""")


#Create Submit Function
def submit():
    con = sqlite3.connect('Customer Information.db')
    cursor = con.cursor()
    con.commit()
    #con.close()

    #INSERT INTO TABLES
    cursor.execute("INSERT INTO Customers Values(:id,:full_name,:home_address,:phone,:email,:items_ordered,:amount_paid,:delivery_address)",
                 {
                    'id':id.get(),
                    'full_name':full_name.get(),
                    'home_address':home_address.get(),
                    'phone':phone.get(),
                    'email': email.get(),
                    'items_ordered':items_ordered.get(),
                    'amount_paid':amount_paid.get(),
                    'delivery_address':delivery_address.get()
                 })
        
def query():
    return

    
    con = sqlite3.connect('Customer Information.db')
    cursor = con.cursor()

    #query
    cursor.execute("SELECT*, old FROM Customer")
    records = cursor.fetchall()
    print(records)

    con.commit()

    #con.close()





    # Clear text boxes
    id.delete(0,END)
    full_name.delete(0,END)
    home_address.delete(0,END)
    phone.delete(0,END)
    email.delete(0,END)
    items_ordered.delete(0,END)
    amount_paid.delete(0,END)
    delivery_address.delete(0,END)


    


id=Entry(root,width=50,font=('Arial',14))
id.grid(row=0,column=1,padx=20,columnspan=2)
full_name = Entry(root,width=50,font=('Arial',14))
full_name.grid(row=1,column=1,columnspan=2)
home_address=Entry(root,width=50,font=('Arial',14))
home_address.grid(row=2,column=1,columnspan=2)
phone=Entry(root,width=50,font=('Arial',14))
phone.grid(row=3,column=1,columnspan=2)
email=Entry(root,width=50,font=('Arial',14))
email.grid(row=4,column=1,columnspan=2)
items_ordered=Entry(root,width=50,font=('Arial',14))
items_ordered.grid(row=5,column=1,columnspan=2)
amount_paid=Entry(root,width=50,font=('Arial',14))
amount_paid.grid(row=6,column=1,columnspan=2)
delivery_address=Entry(root,width=50,font=('Arial',14))
delivery_address.grid(row=7,column=1,columnspan=2)

#Create Text Box labels
id_label =Label(root,text="ID")
id_label.grid(row=0,column=0,padx=10,pady=10)
full_name_label =Label(root,text="Full Name")
full_name_label.grid(row=1,column=0,padx=10,pady=10)
address_label =Label(root,text="Address")
address_label.grid(row=2,column=0,padx=10,pady=10)
phone_label =Label(root,text="Phone")
phone_label.grid(row=3,column=0,padx=10,pady=10)
email_label =Label(root,text="Email")
email_label.grid(row=4,column=0,padx=10,pady=10)
items_ordered_label =Label(root,text="Itemsordered")
items_ordered_label.grid(row=5,column=0,padx=10,pady=10)
amount_paid_label =Label(root,text="Amountpaid")
amount_paid_label.grid(row=6,column=0,padx=10,pady=10)
delivery_address_label =Label(root,text="Delivery Address")
delivery_address_label.grid(row=7,column=0,pady=10,padx=10)

#Create Submit Button
submit_btn = Button(root,text="Add Record to Database",command= submit)
submit_btn.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=200)

#create a query button
query_btn = Button(root,text='Show Records',command=query)
query_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=137)



con.commit()

#con.close()



root.mainloop()