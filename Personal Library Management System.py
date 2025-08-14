from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog
import tkinter as tk
import csv
import os

class Book:
    def __init__(self,title,author,genre,year):
        self.title=title
        self.author=author
        self.genre=genre
        self.year=year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year} - Genre : {self.genre})"
    

class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book) 
                return True
        else:
            return False
    
    def search_book(self,keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]

    
    def save_to_file(self, filename="library.csv"):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for book in self.books:
                writer.writerow([book.title, book.author, book.genre, book.year])

    def load_from_file(self, filename="library.csv"):
        if not os.path.exists(filename):
            return
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 4:
                    self.books.append(Book(*row))



class LibraryGUI:
    def __init__(self,root):
        self.library=Library()
        self.library.load_from_file()
        self.root=root
        self.root.geometry("1057x595+200+175")
        self.root.title("📚 Personal Libarary Management System")
        self.root.resizable(False,False)
        
        self.image_bakground = Image.open(r"C:\Users\Mohamed\OneDrive\Desktop\image2.jpg") 
        self.image_bakground=self.image_bakground.resize((1057,595))
        self.image_bakground= ImageTk.PhotoImage(self.image_bakground)
        self.background=Label(self.root,image=self.image_bakground,bd=0)
        self.background.place(x=0,y=0)
        
        self.var_title=StringVar()
        self.var_author=StringVar()
        self.var_genre=StringVar()
        self.var_year=StringVar()

     # ------------------- Entry --------------------
        self.title_entry=Entry(
            self.root,font=("arial",12),relief="flat",highlightthickness=1,
                highlightbackground="gray",highlightcolor="cyan"
                ,selectbackground="cyan",selectforeground="black"
                ,bd=0,textvariable=self.var_title)
        self.title_entry.place(x=165,y=207,width=200,height=25)
         
        
        self.author_entry=Entry(
            self.root,font=("arial",12),relief="flat",highlightthickness=1,
                highlightbackground="gray",highlightcolor="cyan"
                ,selectbackground="cyan",selectforeground="black"
                ,bd=0,textvariable=self.var_author)
        self.author_entry.place(x=198,y=260,width=200,height=25)
        

        self.genre_entry=Entry(
            self.root,font=("arial",12),relief="flat",highlightthickness=1,
                highlightbackground="gray",highlightcolor="cyan"
                ,selectbackground="cyan",selectforeground="black"
                ,bd=0,textvariable=self.var_genre)
        self.genre_entry.place(x=188,y=315,width=200,height=25)


        self.year_entry=Entry(
            self.root,font=("arial",12),relief="flat",highlightthickness=1,
                highlightbackground="gray",highlightcolor="cyan"
                ,selectbackground="cyan",selectforeground="black"
                ,bd=0,textvariable=self.var_year)
        self.year_entry.place(x=168,y=367,width=200,height=25)
     
     # ------------------- Button --------------------
       
        
        self.add=Button(self.root,text="Add",background="#FFA500",
          fg="white",font=("arial",14),activebackground="#FFA500",
          activeforeground="white",relief="flat",bd=0,command=self.bt_add_books)
        
        

        self.remove=Button(self.root,text="Remove",background="#FFA500",
          fg="white",font=("arial",14),activebackground="#FFA500",
          activeforeground="white",relief="flat",bd=0,command=self.bt_remove_book)
        

        self.search=Button(self.root,text="search",background="#FFA500",
          fg="white",font=("arial",14),activebackground="#FFA500",
          activeforeground="white",relief="flat",bd=0,command=self.bt_search_books)
        

        self.display=Button(self.root,text="Display",background="#FFA500",
          fg="white",font=("arial",14),activebackground="#FFA500",
          activeforeground="white",relief="flat",bd=0,command=self.bt_display_books)
        
        self.add.place(x=70,y=415,width=70,height=30)
        self.remove.place(x=160,y=415,width=80,height=30)
        self.search.place(x=260,y=415,width=80,height=30)
        self.display.place(x=360,y=415,width=80,height=30)
        
       
     # ------------------ Listbox -------------
        self.list1=Listbox(self.root,bg="black",highlightbackground="black"
                           ,highlightcolor="black",fg="white",relief="flat",bd=0,selectbackground="cyan",font=("arail",10),selectmode=SINGLE)

        self.list1.place(x=515,y=227,width=470,height=230)


        self.add.bind("<Enter>",self.bt_add_enter)
        self.add.bind("<Leave>",self.bt_add_leave)
        self.remove.bind("<Enter>",self.bt_remove_enter)
        self.remove.bind("<Leave>",self.bt_remove_leave)
        self.search.bind("<Enter>",self.bt_search_enter)
        self.search.bind("<Leave>",self.bt_search_leave)
        self.display.bind("<Enter>",self.bt_display_enter)
        self.display.bind("<Leave>",self.bt_display_leave)
        self.bt_display_books()


    def bt_add_enter(self,e):
        self.add.config(background="#BF9548")

    def bt_add_leave(self,e):
        self.add.config(background="#FFA500")

    def bt_remove_enter(self,e):
        self.remove.config(background="#BF9548")

    def bt_remove_leave(self,e):
        self.remove.config(background="#FFA500")

    def bt_search_enter(self,e):
        self.search.config(background="#BF9548")

    def bt_search_leave(self,e):
        self.search.config(background="#FFA500")

    def bt_display_enter(self,e):
        self.display.config(background="#BF9548")

    def bt_display_leave(self,e):
        self.display.config(background="#FFA500")
    

    def bt_add_books(self):
        title=self.var_title.get()
        author=self.var_author.get()
        genre=self.var_genre.get()
        year=self.var_year.get()

        if not (title and author and genre and year):
            messagebox.showerror("Error","All fields are required.")
            return
        
        book =Book(title,author,genre,year)
        self.library.add_book(book)
        self.library.save_to_file()
        self.bt_display_books()
        self.clear_entries()
        messagebox.showinfo("Success", "Book added.")
    
    def bt_search_books(self):
        keyword =simpledialog.askstring("Search","Enter title or author:")
        if not keyword:
            messagebox.showinfo("Error","NO, Title Or Author Enter")
        result = self.library.search_book(keyword)
        self.list1.delete(0, END)
        for book in result:
            self.list1.insert(END, str(book))
        if not result:
            messagebox.showinfo("Search", "No books found.")

    def bt_remove_book(self):
        selected = self.list1.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a book to remove.")
            return
        book_str = self.list1.get(selected[0])
        title = book_str.split(" by ")[0]       #["title","{self.author} ({self.year} - Genre : {self.genre})"]
        if self.library.remove_book(title):
            self.library.save_to_file()
            self.bt_display_books()
            messagebox.showinfo("Removed", "Book removed.")
        else:
            messagebox.showerror("Error", "Book not found.")

    def bt_display_books(self):
        self.list1.delete(0,END)
        for book in self.library.books:
            self.list1.insert(END, str(book))
    

    def clear_entries(self):
        self.title_entry.delete(0, END)
        self.author_entry.delete(0, END)
        self.genre_entry.delete(0, END)
        self.year_entry.delete(0, END)


class PersonalLibraryManagmentSystem(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1057x595+200+175")
        self.title("📚 Personal Libarary Management System")
        image_bakground = Image.open(r"C:\Users\Mohamed\Downloads\Updated_Library_Image_With_Clean_Smaller_Icon.png") 
        image_bakground=image_bakground.resize((1057,595))
        self.image_bakground= ImageTk.PhotoImage(image_bakground)
        self.background=Label(self,image=self.image_bakground)
        self.background.place(x=0,y=0)
        self.lbl_hello=Label(self,text="Hello :)",font=("arial",18,"bold"),relief="flat",bd=0,background="#D2D2D2")
        self.lbl_hello.place(x=755,y=250)
        self.lbl_scentence=Label(self,text="'Books are the quietest and most constant of friends'",font=("arial",18,"bold"),relief="flat",bd=0,background="white")
        self.lbl_scentence.place(x=200,y=520)
        self.lbl_username=Label(self,text="Username :",font=("arial",13,"bold"))
        self.lbl_username.place(x=640,y=300)
        self.lbl_password=Label(self,text="Password :",font=("arial",13,"bold"))
        self.lbl_password.place(x=640,y=350)
        self.var_user=StringVar()
        self.var_pass=StringVar()
        self.username_input=Entry(self,font=("arial",12),relief="flat",highlightthickness=1,
                highlightbackground="gray",highlightcolor="cyan"
                ,selectbackground="cyan",selectforeground="black"
                ,bd=0,textvariable=self.var_user)
        self.password_input=Entry(self,font=("arial",12),relief="flat",highlightthickness=1,
                highlightbackground="gray",highlightcolor="cyan"
                ,selectbackground="cyan",selectforeground="black",show="*"
                ,textvariable=self.var_pass,bd=0)
        self.username_input.place(x=740,y=300)
        self.password_input.place(x=740,y=350)
        self.login=Button(self,text="Login",background="#FFA500",
          fg="white",font=("arial",14),activebackground="#FFA500",
          activeforeground="white",relief="flat",bd=0,command=self.login_click)
        

        self.signup=Button(self,text="SignUp",background="#FFA500",
          fg="white",font=("arial",14),activebackground="#FFA500",
          activeforeground="white",relief="flat",bd=0,command=self.signup_click)
       
        self.login.bind("<Enter>",self.bt_login_enter)
        self.login.bind("<Leave>",self.bt_login_leave)
        self.signup.bind("<Enter>",self.bt_signup_enter)
        self.signup.bind("<Leave>",self.bt_signup_leave)
        self.login.place(x=700,y=400,width=90,height=30)
        self.signup.place(x=810,y=400,width=90,height=30) 

    def bt_login_enter(self,e):
        self.login.config(background="#BF9548")

    def bt_login_leave(self,e):
        self.login.config(background="#FFA500")

    def bt_signup_enter(self,e):
        self.signup.config(background="#BF9548")

    def bt_signup_leave(self,e):
        self.signup.config(background="#FFA500")

       
   
    def login_click(self):
        user = self.var_user.get()
        pas = self.var_pass.get()
        if user.lower()=="mohamed" and pas=="12345":
            self.destroy()
            root = tk.Tk()
            app = LibraryGUI(root)
            app.mainloop()
            
            # ------------------ "Otherwise" -------------
            """win = tk.Toplevel(self)  
            app = LibraryGUI(win)
            self.withdraw()"""
        else:
            messagebox.showerror("Error" ,"The username not Register plz SignUP")
    def signup_click(self):
        pass



AppLib=PersonalLibraryManagmentSystem()
AppLib.resizable(False,False)
AppLib.mainloop()