from tkinter import *
from  tkinter import messagebox
from math import  gcd

class Main():
    def __init__(self,root,shifr):
        self.root=root
        Design_window(root)
        if shifr:
            Button_for_1(root)
        else:
            Button_for_2(root)

class Design_window(Main):
    def __init__(self,root):
        self.alfa = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.number = [i + 1 for i in range(26)]

        self.name=Label(root, text="Input text:", font="Arial 20").place(x=10,y=10)
        self.input_1 = Entry(root)
        self.input_1.place(x=150,y=20)
        self.mod = Label(root, text="Input mod:", font="Arial 20").place(x=10,y=80)
        self.input_2 = Entry(root)
        self.input_2.place(x=150,y=90)
        self.key = Label(root, text="Input key:", font="Arial 20").place(x=10,y=150)
        self.input_3 = Entry(root)
        self.input_3.place(x=150,y=160)

class Button_for_1(Design_window):
    def __init__(self,root):
        Design_window.__init__(self,root)
        button_1 = Button(root, text='Execute',font="Arial 22" , command=self.check, width=12,
                               height=2).place(x=10,y=220)
        button_2 = Button(root, text='Exit',font="Arial 22" , command=root.destroy, width=12,
                               height=2).place(x=250,y=220)
    def check(self):
        name =self.input_1.get()
        mod = self.input_2.get()
        key = self.input_3.get()
        new_name = []

        letter=int(mod)/gcd(int(key),int(mod))
        for i in name:
            math = (self.alfa.index(i)+1) * int(key) % int(mod)
            new_name.append(self.alfa[math - 1])
        new_name = ''.join(new_name)
        Dialog_window(key,mod)
        Create_add_window(name,new_name,'i=index*key%mod','en',int(letter))

class Button_for_2(Design_window):
    def __init__(self, root):
        Design_window.__init__(self, root)
        button_1 = Button(root, text='Execute', font="Arial 22", command=self.check, width=12,
                          height=2).place(x=10, y=220)
        button_2 = Button(root, text='Exit', font="Arial 22", command=root.destroy, width=12,
                          height=2).place(x=250, y=220)

    def check(self):
        name = self.input_1.get()
        mod = self.input_2.get()
        key = self.input_3.get()
        old_name = []


        for i in name:
            for j in self.number:
                letter = j * int(key) % int(mod)
                if letter == self.alfa.index(i)+1:
                    old_name.append(self.alfa[j - 1])
                    break

        old_name = ''.join(old_name)
        Dialog_window(key,mod)
        Create_add_window(name,old_name, '(i+mod-k)% mod','de')


class Dialog_window():
    def __init__(self,key,mod):
        if gcd(int(key),int(mod))==1:
            pass
        else:
            answer = messagebox.askyesno(title='Answer', message='Do you want to continue?')
            if answer:
                pass
            else:
                sys.exit()


class Create_add_window():
 def __init__(self,start_name,after_name,formula,word,letter=None):
    new_window=Tk()
    new_window.geometry("500x250")
    new_window.title("Add_window")

    outpt_1 = Label(new_window, text=str(formula), font="Arial 20").place(x=150, y=10)

    outpt_2 = Label(new_window, text="Start text:", font="Arial 20").place(x=10, y=60)
    outpt_3 = Label(new_window, text="Text after " + str(word) + "cryption:", font="Arial 20").place(x=10, y=100)

    outpt_4 = Label(new_window, text="Letter:" + str(letter),
                    font="Arial 20").place(x=10, y=140)

    input_1 = Entry(new_window)
    input_1.place(x=135, y=70)
    input_1.insert(1,start_name)

    input_2 = Entry(new_window)
    input_2.place(x=270, y=115)
    input_2.insert(1,after_name)


if __name__=="__main__":
    root_1=Tk()
    root_2=Tk()
    win_1=Main(root_1,True)
    win_2 = Main(root_2,False)
    root_1.title("First_window")
    root_2.title("Second_window")
    root_1.geometry("500x400")
    root_2.geometry("500x400+625+185")
    root_1.mainloop()
    root_2.mainloop()
