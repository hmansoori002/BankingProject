from tkinter import Tk, Frame, Button, Label,Entry
import connect
import operateaccount


class Delete :
    con=''
    def __init__(self, root, msg):
        self.root = root
        self.msg = msg
        self.root.title("Delete Record")
        self.root.geometry("700x600")

        self.head=Label(self.root, text="Delete Record :  ",
                                    fg='red',
                                    font='Times 25')

        self.l1 = Label(self.root, text="Accno : ",
                             fg='blue',
                             font="Times 25")
        
        self.e1=Entry(self.root, width=20,
                                      font='Times 25')

        self.b1 = Button(self.root ,text="Delete Record",
                                     width=20 , height=2,
                                      bg='light blue',
                                    command=self.nextFrame)
        
        self.b2=Button(self.root , text="Exit",
                       bg="red", width=20 , height=2,
                       command=self.exitWindow)

        self.b3=Button(self.root , text="Back",
                       width=20 , height=2,
                       bg='light blue',
                       command=self.backWindow)

        self.l4 = Label(self.root, textvariable=self.msg,
                        fg='red', font="Times 20")

        self.head.place(x=200,y=50)
        self.l1.place(x=100,y=110)
        self.e1.place(x=300,y=110)
        self.b1.place(x=200,y=200)
        self.b3.place(x=400,y=200)
        self.b2.place(x=300,y=300)
        self.l4.place(x=100,y=400)

    def exitWindow(self):
        self.root.destroy()
        return

    def backWindow(self):
        self.root.destroy()
        back=Tk()
        operateaccount.TakeOperation(back)
        return

    def nextFrame(self):
        ano = self.e1.get()
        if ano=='':
            self.msg.set("Accno field cannot be empty")
        else:
            try:
                Delete.con = connect.DBConnect.getConn()
                print("Connected to database")
                cur=Delete.con.cursor()
                cur.execute("delete from account where AccNo="+ano)
                Delete.con.commit()
                self.msg.set("Successfully Deleted")
            except Exception as msg:
                print("Invalid Account....")
            finally:
                if Delete.con !='':
                    Delete.con.close()
                    print("Connection released")
        return
    
            
            
            











            

        

       
