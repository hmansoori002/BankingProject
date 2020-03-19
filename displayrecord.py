from tkinter import Tk, Frame, Button, Label,Entry,StringVar
import connect
import operateaccount

class Display :
    con=''
    def __init__(self, root, msg):
        self.root = root
        self.msg = msg
        self.root.title("Display Record")
        self.root.geometry("700x600")
        self.res1=StringVar()
        self.res2=StringVar()

        self.head = Label(self.root, text="Account Information : ",
                             fg='red',
                             font="Times 30")

        self.l1 = Label(self.root, text="Accno : ",
                             fg='blue',
                             font="Times 25")

        self.e1 = Entry(self.root, width=20, font=" Times 25")

        self.b1 = Button(self.root, text="Display",
                             width=20, height=2,
                             bg='light blue',
                             command=self.nextFrame)

        self.l2 = Label(self.root, text="Name : ",
                             fg='blue',
                             font="Times 25")
        
        self.e2 = Entry(self.root, width=20,
                        font="Times 25" , textvariable=self.res1)

        self.l3 = Label(self.root, text="Balance : ",
                             fg='blue',
                             font="Times 25")
        
        self.e3 = Entry(self.root, width=20,
                        font="Times 25" , textvariable=self.res2)

        self.b2 = Button(self.root, text="Exit",
                             width=20, height=2,
                             bg='light blue',
                             command=self.exitWindow)

        self.l4 = Label(self.root, textvariable=self.msg,
                        fg='red', font="Times 20")

        self.b3=Button(self.root , text="Back",
                       width=20 , height=2,
                       bg='light blue',
                       command=self.backWindow)

        self.head.place(x=200,y=50)
        self.l1.place(x=100,y=110)
        self.e1.place(x=300,y=110)
        self.l2.place(x=100,y=250)
        self.e2.place(x=300,y=250)
        self.l3.place(x=100,y=350)
        self.e3.place(x=300,y=350)
        self.b1.place(x=250,y=180)
        self.b2.place(x=150,y=430)
        self.l4.place(x=100,y=500)
        self.b3.place(x=350,y=430)
        
    def nextFrame(self):
        ano = self.e1.get()
        if ano=='':
            self.msg.set("accno field cannot be empty")
        else:
            try:
                Display.con=connect.DBConnect.getConn()
                print("Connected to database")
                cur = Display.con.cursor()
                cur.execute("select Name , Balance from account where AccNo="+ano)
                record=cur.fetchone()
                self.res1.set(record[0])
                self.res2.set(record[1])
                self.msg.set("Thanks For Visiting....")
            except Exception as msg:
                self.msg.set("Invalid Account no. ....Try again...")
            finally:
                if Display.con != '':
                    Display.con.close()
                    print("Connection Released....")
            return

    def backWindow(self):
        self.root.destroy()
        back=Tk()
        operateaccount.TakeOperation(back)
        return
            
    def exitWindow(self):
        self.root.destroy()
        return
    
