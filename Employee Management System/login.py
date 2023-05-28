from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'enter all the details')

    elif usernameEntry.get() == 'Sowmya' and passwordEntry.get() == '2002':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import employee

    else:
        messagebox.showerror('Error', 'Please enter correct credentials')


window = Tk()

window.geometry('1550x800+0+0')
window.title('employee page')
backgroundimage=ImageTk.PhotoImage(file='pic.jpg')
bgLabel=Label(window,image=backgroundimage)
bgLabel.place(x=0,y=0)


loginFrame = Frame(window, bg='white')
loginFrame.place(x=250, y=250)

textLabel = Label(loginFrame, text='EMPLOYEE MANAGEMENT                          ', compound=LEFT
                  , font=('times new roman', 20, 'bold'), bg='white')
textLabel.grid(row=0, column=1, pady=10, padx=10)

usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame, image=usernameImage, text='Username', compound=LEFT
                      , font=('times new roman', 20, 'bold'), bg='white')
usernameLabel.grid(row=2, column=0, pady=5, padx=5)

usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='black')
usernameEntry.grid(row=2, column=1, pady=5, padx=5)

passwordImage = PhotoImage(file='password.png')
passwordLabel = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT
                      , font=('times new roman', 20, 'bold'), bg='white')
passwordLabel.grid(row=3, column=0, pady=5, padx=5)

passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5, fg='black')
passwordEntry.grid(row=3, column=1, pady=5, padx=5)

loginButton = Button(loginFrame, text='Login', font=('times new roman', 14, 'bold'), width=5
                     , fg='white', bg='black', activebackground='white',
                     activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=4, column=1, pady=20)

window.mainloop()