import customtkinter
from tkinter import * 

root = customtkinter.CTk()
root.title("Login")
root.geometry("1000x600")
customtkinter.set_appearance_mode("dark")
root.resizable(False, False)
root.iconbitmap("logo1.ico")


side_bar = customtkinter.CTkFrame(root, width=240, height = 600, corner_radius=10)
side_bar.place(x  =0, y = 0)

button1 = Button(master=side_bar, borderwidth = 0, width=20, height = 2 , fg="#9e9e9e", text="Profile", bg='#242424', font=('Rod',15,'bold'))
button1.place(x = 25, y = 95)



root.mainloop()


