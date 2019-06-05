from tkinter import *

root = Tk(className="My first window")
root.config(bg="black", width=1200, height=500)
root.resizable(0, 0)
labelEmail = Label(root)
labelEmail.place(x=10, y=40)
labelEmail.config(width=10, height=1, text="EMAIL", bg="#ddd", fg="#222")

email = Entry(root)
email.place(x=100, y=40)
email.config(width=30, justify="center")

labelPassword = Label(root)
labelPassword.place(x=10, y=90)
labelPassword.config(width=10, height=1, text="PASSWORD", bg="#ddd", fg="#222", )

password = Entry(root)
password.place(x=100, y=90)
password.config(width=30,justify="center", show="*")

sendValue = Button(root)
sendValue.place(x=100, y=130)
sendValue.config(width=16, height=1, text="Enviar", bg="blue", fg="white", bd=0)

frame = Frame(root)
frame.place(x=500, y=0)
frame.config(bg="orange", width=700, height=250)

labelRegister = Label(frame)
labelRegister.place(x=0, y=0)
labelRegister.config(width=70, height=3, bg="#ddd", text="Usuarios registrados", fg="#222", font="Verdana")


frameBanner = Frame(root)
frameBanner.place(x=0, y=300)
frameBanner.config(width=1200, height=200, bg="red")


labelBanner = Label(frameBanner)
labelBanner.place(x=0, y=0)

labelBanner.config(width=120, height=2, bg="orange", text="Usuarios no registrados", font="Verdana")






# frame = Frame(root)
# frame.place(x=390, y=0)
# frame.config(bg="#ddd", width=500, height=500)

# label = Label(frame)
# label.place(x=0, y=50)
# label.config(text="BANKING ACCOUNT", fg="#ddd", bg="#222", width=50, height=2, font="Verdana", bd=0, justify="center")

# label2 = Label(frame)
# label2.place(x=0, y=150)
# label2.config(text="Email", fg="#222", bg="#d1d1d1", width=50, height=2, font="Verdana", bd=0, justify="center")

# textEmail = Entry(frame)
# textEmail.place(x=120, y=200, width=300, height=35)
# textEmail.config(font="Verdana", fg="#222")
 

# textPassword = Entry(frame)
# textPassword.place(x=120, y=240, width=300, height=35)
# textPassword.config(font="Verdana", fg="#222", show=".", justify="center")

# buttonStart = Button(frame)
# buttonStart.place(x=180, y=300)
# buttonStart.config(width=20, height=2, bg="blue", fg="white", text="Start session")

# buttonRegister = Button(frame)
# buttonRegister.place(x=316, y=470)
# buttonRegister.config(width=20, height=1, bg="red", fg="white", text="Register")

 













base = root.mainloop()










