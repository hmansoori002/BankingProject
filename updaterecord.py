from tkinter import Tk, Frame, Button, Label , Entry
import connect
import operateaccount
 

class Update :
    con=''
    def __init__(self, root, msg):
        self.root = root
        self.msg = msg
        self.root.title("Update Record")
        self.root.geometry("700x600")

        self.head = Label(self.root, text="Update Records : ",
                             fg='red',
                             font="Times 30")

        self.l1 = Label(self.root, text="Accno : ",
                             fg='blue',
                             font="Times 25")

        self.e1 = Entry(self.root, width=20,
                        font=" Times 25")

        self.l2 = Label(self.root, text="New Name : ",
                             fg='blue',
                             font="Times 25")
        
        self.e2 = Entry(self.root, width=20,
                        font="Times 25")

        self.l3 = Label(self.root, text="New Balance : ",
                             fg='blue',
                             font="Times 25")
        
        self.e3 = Entry(self.root, width=20,
                        font="Times 25")
        
        self.b1 = Button(self.root, text="Update",
                             width=20, height=2,
                             bg='light blue',
                             command=self.nextFrame)

        self.b2 = Button(self.root, text="Exit",
                             width=20, height=2,
                             bg='light blue',
                             command=self.exitWindow)
        
        self.l4 = Label(self.root, textvariable=self.msg,
                        fg='red', font="Times 30")

        self.b3=Button(self.root , text="Back",
                       width=20 , height=2,
                       bg='light blue',
                       command=self.backWindow)

        self.head.place(x=200,y=50)
        self.l1.place(x=100,y=110)
        self.e1.place(x=300,y=110)
        self.l2.place(x=100,y=220)
        self.e2.place(x=300,y=220)
        self.l3.place(x=100,y=330)
        self.e3.place(x=300,y=330)
        self.b1.place(x=150,y=400)
        self.b2.place(x=250,y=450)
        self.l4.place(x=100,y=500)
        self.b3.place(x=350,y=400)

    def nextFrame(self):
        ano = self.e1.get()
        name = self.e2.get()
        amount = self.e3.get()

        if ano=='':
            self.msg.set("accno field cannot be empty")
        elif amount=='':
            self.msg.set("amount field cannot be empty")
        else:
            try:
                Update.con = connect.DBConnect.getConn()
                print("Connected to database")
                cur = Update.con.cursor()
                if(name==''):
                    cur.execute("update account set Balance="+amount+" where AccNo="+ano)
                else:
                    cur.execute("update account set Name='"+name+"' , Balance="+amount+" where AccNo="+ano)
                Update.con.commit()
                self.msg.set("Successfully Updated......")
            finally:
                if Update.con != '':
                    Update.con.close()
                    print("Connection released")
        return

    def backWindow(self):
        self.root.destroy()
        back=Tk()
        operateaccount.TakeOperation(back)
        return
    

    def exitWindow(self):
        self.root.destroy()
        return
      

