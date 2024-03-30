'MR_Ali_mj'

class Address:

    def __init__(self, city, street, zip_code):
        self.city = city
        self.street = street
        self.zip_code = zip_code
 
    def __str__(self):
        return f'City : {self.city} \n Street : {self.street} \n zip_code : {self.zip_code}'
    
class Category:

    def __init__(self,category) -> None:
        self.category = category

    def __str__(self) -> str:
        return f"{self.category}"
class Contact:
    def __init__(self,telphone='') -> None:
        self.__telphone = telphone
        self.email = None
    @property
    def telphone(self):
        return self.__telphone
    @telphone.setter

    def telphone(self,value):
        if (len(value) == 11):
            print('conact added .')
            self.__telphone == value
        else:
            print('please try again !')
            self.__telphone == ''
            
    def __str__(self) -> str:
        return f"{self.telphone} \n Email: {self.email}"
    
class Person:

    def __init__(self,fname ,lname ,email,category ,contact):
        self.firstname = fname
        self.lastname = lname
        self.email = email
        self.address = None
        self.contact = Contact(contact)
        self.category = Category(category)
        
    def __str__(self) -> str:
        return f" name : {self.firstname} {self.lastname} \n email :{self.email} \n address: {self.address} \n category : {self.category} \n  telphone : {self.contact}"
    
from tkinter import *

class PhoneBook :
    
    def __init__(self ,master) -> None:
        frame = Frame(master)
        frame.pack()

        self.welcome = Label(master , text='Welcome !',bg='whitesmoke')
        self.welcome.pack(pady=20)

        self.fname = Label(master ,text='FirstName :',bg='whitesmoke')
        self.fname.place(x= 90,y=50)

        global fname
        fname = StringVar()
        self.fname_ent = Entry(master,textvariable=fname)
        self.fname_ent.place(x = 160 ,y= 50)

        self.lname = Label(master,text='LastName :',bg='whitesmoke')
        self.lname.place(x= 90 , y= 80 )

        global lname
        lname = StringVar()
        self.lname_ent = Entry(master,textvariable=lname)
        self.lname_ent.place(x= 160 ,y=80)

        category = Label(master ,text='select your category 1)Family 2)coworker 3)firends',bg='whitesmoke')
        category.place(x=90,y=120)

        global cate
        cate = StringVar()
        self.category_ent = Entry(master,textvariable=cate)
        self.category_ent.place(x=90,y=140)

        self.contact = Label(master ,text='enter telphone number :',bg='whitesmoke')
        self.contact.place(x=90,y=160)

        global contact
        contact = StringVar()
        contact_ent = Entry(master,textvariable=contact)
        contact_ent.place(x=230,y=160)

        self.email = Label(master,text='Email :',bg='whitesmoke')
        self.email.place(x=90,y=180)

        global email
        email = StringVar()
        self.email_ent = Entry(master,textvariable=email)
        self.email_ent.place(x=140,y=180)

        self.sumbit = Button(master,text='sumbit',bg='whitesmoke',command=Sumbit )
        self.sumbit.place(x=180,y=220)

        self.exit = Label(master,text='please press the exit >>>',bg='whitesmoke')
        self.exit.place(x= 90 ,y= 250)

    def Adderss():
      
        master = Tk()
        master.title('Address')
        master.geometry('400x400')
        master.config(background='whitesmoke')
        address = Label(master ,text='do you like add address for your contact ? yes / no ',bg='whitesmoke')
        address.place(x=90,y=30)
      
        global addre
        addre = StringVar()
        address_ent = Entry(master,textvariable=addre)
        address_ent.place(x=90,y=50)

        submit = Button(master,text='submit',bg='whitesmoke',command=Adderss_sumbit)
        submit.place(x=180,y=80)

        exit = Label(master,text='After Answer To Address You Must Press To Exit >> ',bg='whitesmoke')
        exit.place(x=90 ,y=120 )

        exit_but = Button(master,text='exit',bg='whitesmoke',command= master.destroy)
        exit_but.place(x=180,y=150)

        master.mainloop()

    def answer_address():

        windows = Tk()
        windows.title('Address')
        windows.geometry('400x400')
        windows.config(background='whitesmoke')
        windows.resizable(False,False)

        if addres == 'yes' :

            welcome = Label(windows,text='Welcome',bg='whitesmoke')
            welcome.pack(pady=20)
        
            city = Label(windows,text='city :',bg='whitesmoke')
            city.place(x=90,y=50)

            global City
            City = StringVar()
            city_ent = Entry(windows,textvariable=City)
            city_ent.place(x=135,y=50)

            street = Label(windows,text='street :',bg='whitesmoke')
            street.place(x=90,y=80)

            global Street
            Street = StringVar()
            street_ent = Entry(windows,textvariable=Street)
            street_ent.place(x=140,y=80)

            zip_code = Label(windows,text='zip_code :',bg='whitesmoke')
            zip_code.place(x=90,y=110)

            global Zip_code
            Zip_code = StringVar()
            zip_code_ent = Entry(windows,textvariable=Zip_code)
            zip_code_ent.place(x=160,y=110)

            sumbit = Button(windows,text='Sumbit',bg='whitesmoke',command=answer_sumbit)
            sumbit.place(x=180,y=140)

            update_le = Label(windows,text='do you like Update your contact ? >>>',bg='whitesmoke')
            update_le.place(x=90,y=170)

            global update
            update = StringVar()
            update_ent = Entry(windows,textvariable=update)
            update_ent.place(x=90,y=190)

            update_sumbit = Button(windows,text='Update',bg='whitesmoke',command=Upsumbit)
            update_sumbit.place(x=180,y=210)
        elif addre == 'no' :
            object.address = Address('','','')
        else:
            pass

        windows.mainloop()
    
    def Update_Contact():

        root = Tk()
        root.title('Update_contact')
        root.geometry('400x400')
        root.config(background='whitesmoke')
        root.resizable(False,False)

        root2 = Tk()
        root2.title('update')
        root2.geometry('400x400')
        root2.resizable(False,False)
        root2.config(background='whitesmoke')

        if Update == 'yes' :

            welcome = Label(root,text='Welcome',bg='whitesmoke')
            welcome.pack(pady=20)

            show = Label(root,text='select your choose and edit >>>',bg='whitesmoke')
            show.place(x=90,y=50)

            user = Label(root,text='1)Name  2)Lname  3)Category  4)Telphone  5)Email  6)Address ',bg='whitesmoke')
            user.place(x=35,y=70)

            global User
            User = StringVar()
            user_ent = Entry(root,textvariable=User)
            user_ent.place(x=90,y=90)

            sumbit = Button(root,text='Sumbit',bg='whitesmoke',command=Sumbit_up)
            sumbit.place(x=180,y=120)

        elif up == 'no' :
            end = Label(root2,text='thank you for register your contact in PhoneBook ;) .',bg='whitesmoke')
            end.place(x= 90,y= 20)
            
            exit = Button(root2,text='Exit',bg='whitesmoke',command=root.destroy).place(x= 180,y=50)

            root2.mainloop()
        root.mainloop()

    def Update():

        root = Tk()
        root.title('Update_contact')
        root.geometry('400x400')
        root.config(background='whitesmoke')
        root.resizable(False,False)

        if User == '1' :
            name  = Label(root,text='NewName :',bg='whitesmoke').place(x= 90,y= 70)
            
            global name_var
            name_var = StringVar()
            name_ent = Entry(root,textvariable=name_var).place(x= 150,y= 70)

            sumbit = Button(root,text='sumbit',command=Enter1,bg='whitesmoke').place(x= 180,y= 140)

        elif User == '2':
            lname  = Label(root,text='NewLastName :',bg='whitesmoke').place(x= 90,y= 70)
            
            global lname_var
            lname_var = StringVar()
            lname_ent = Entry(root,textvariable=lname_var).place(x= 150,y= 70)

            sumbit = Button(root,text='sumbit',command=Enter2,bg='whitesmoke').place(x= 180,y= 140)

        elif User == '3':
            category  = Label(root,text='NewCategory :',bg='whitesmoke').place(x= 90,y= 70)
            
            global category_var
            category_var = StringVar()
            category_ent = Entry(root,textvariable=category_var).place(x= 150,y= 70)

            sumbit = Button(root,text='sumbit',command=Enter3,bg='whitesmoke').place(x= 180,y= 140)

        elif User == '4':
            telphone  = Label(root,text='NewTelphone :',bg='whitesmoke').place(x= 90,y= 70)
            
            global telphone_var
            telphone_var = StringVar()
            telphone_ent = Entry(root,textvariable=telphone_var).place(x= 150,y= 70)

            sumbit = Button(root,text='sumbit',command=Enetr4,bg='whitesmoke').place(x= 180,y= 140)

        elif User == '5':
            Email  = Label(root,text='NewEmail :',bg='whitesmoke').place(x= 90,y= 70)
            
            global email_var
            email_var = StringVar()
            email_ent = Entry(root,textvariable=email_var).place(x= 150,y= 70)

            sumbit = Button(root,text='sumbit',command=Enter5,bg='whitesmoke').place(x= 180,y= 140)

        elif User == '6':
            city = Label(root,text='NewCity :',bg='whitesmoke').place(x=90,y=70)

            global city_var
            city_var = StringVar()
            city_ent = Entry(root,textvariable=city_var).place(x=150,y=70)

            street = Label(root,text='NewStreet :',bg='whitesmoke').place(x=90,y=100)

            global street_var
            street_var = StringVar()
            street_ent = Entry(root,textvariable=street_var).place(x=150,y=100)

            zip_code = Label(root,text='NewZipcode :',bg='whitesmoke').place(x=90,y=130)

            global zip_code_var
            zip_code_var = StringVar()
            zip_code_ent = Entry(root,textvariable=zip_code_var).place(x=150,y=130)

            sumbit = Button(root,text='sumbit',command=Enter6,bg='whitesmoke').place(x= 180,y= 140)

        else:
            pass
        root.mainloop()

def Sumbit():
    Name = fname.get()
    Lname = lname.get()
    Category = cate.get()

    if Category == '1' or 'family' :
        categ = 'Family'
    elif Category == '2' or 'coworker' :
        categ = 'Coworker'
    elif Category == '3' or 'firends' :
        categ = 'firends'
    else:
        categ = ''

    cont = contact.get()
    Email = email.get()
    global object
    object = Person(Name,Lname,Email,categ,cont)

def Adderss_sumbit():
    global addres
    addres = addre.get()

def answer_sumbit():
    city = City.get()
    street = Street.get()
    zip_code = Zip_code.get()
    object.address = Address(city,street,zip_code)

def Upsumbit():
    global Update
    Update = update.get()

def update_sumbit():
    global up
    up = User.get()
    
def Sumbit_up():
    global get
    get = User.get()

def Enter1():
    Name = name_var.get()
    object.firstname == Name

def Enter2():
    Lname = lname_var.get()
    object.lastname == Lname

def Enter3():
    category = category_var.get()
    object.category == category

def Enetr4():
    telphone = telphone_var.get()
    object.contact == telphone

def Enter5():
    Email = email_var.get()
    object.email == Email

def Enter6():
    city = city_var.get()
    street = street_var.get()
    zip_code = zip_code_var.get()
    object.address == Address(city,street,zip_code)

def Main():
    window = Tk()
    window.title('PhoneBook')
    window.geometry('400x400')
    window.config(background='whitesmoke')
    window.resizable(False,False)
    q = PhoneBook(window)
    window.mainloop()
    PhoneBook.Adderss()
    PhoneBook.answer_address()
    PhoneBook.Update_Contact()
    print(object)
    

if __name__ == "__main__" :
     Main()
     
'''

The End Project ...

'''