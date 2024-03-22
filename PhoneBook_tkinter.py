'MR_Ali_mj'

class Address:
    def __init__(self, street, city, zip_code):
        self.city = city
        self.street = street
        self.zip_code = zip_code
 
    def __str__(self):
        return f'City : {self.city} \n Street : {self.street} \n zip_code : {self.zip_code} \n '
    
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
    def __init__(self,fname ,lname ,category ,contact):
        self.firstname = fname
        self.lastname = lname
        self.address = None
        self.contact = Contact(contact)
        self.category = Category(category)
        
    def __str__(self) -> str:
        return f" name : {self.firstname} {self.lastname} \n address: {self.address} \n category : {self.category} \n contact details : {self.contact}"
    
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

        # if self.category_ent == '1':
        #     categor2 = 'family'
        # elif self.category_ent == '2':
        #     categor2 = 'coworker'
        # elif self.category_ent == '3':
        #     categor2 = 'firends'
        # else:
        #     categor2 = ''

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

        self.sumbit = Button(master,text='sumbit',bg='whitesmoke',command=Sumbit)
        self.sumbit.place(x=180,y=220) 

def Sumbit():
    name = fname.get()
    Lname = lname.get()
    category = cate.get()
    cont = contact.get()
    Email = email.get()

    object = Person(name,Lname,category,cont)
    object2 = Contact()
    object2.email = Email
    print(object,object2)


        


            


        


'در اخر مقادیر خواسته شده را به دیکشنری یوسر وارد کن '
'aquamarine'




def Main():
    window = Tk()
    window.title('PhoneBook')
    window.geometry('400x400')
    window.config(background='whitesmoke')
    q = PhoneBook(window)
    window.mainloop()

if __name__ == "__main__" :
     Main()