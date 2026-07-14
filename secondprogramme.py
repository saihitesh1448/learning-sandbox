class Book:
    def __init__(self):
        self.title="not entred"
        self.author="not entred"
        self.pages="not entred"
        self.price=None
        self.is_issued=False
    def details(self):
        self.title=input("enter the title of book: ")
        self.author=input("enter the author name of book: ")
        while True:
            self.pages=int(input("enter the no of pages: "))
            if self.pages>0:
                break
            else:
                print("enter valid no of pages")
        while True:
            self.price=float(input("enter the price of book: "))
            if self.price>0:
                break
            else:
                print("enter a valid price")
    def issue(self):
        if self.is_issued:
            print("book is alredy issued")
        else:
            self.is_issued=True
            print("book is now issued")
    def ret(self):
        if self.is_issued:
            self.is_issued=False
            print("book is now returned")
        else:
            print("book is already returned")
    def print_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Price: Rs {self.price}")
        print(f"Status: {'Issued' if self.is_issued else 'Available'}")
    def __str__(self):
        return f"Book title:{self.title}, Book authour:{self.author}, Book price:{self.price}, Book pages:{self.pages}"
    

books=[]
current=None
while True:
    print(".............menue...............\n")
    print("1.enter details\n2.see details\n3.issue book\n4.return book\n5.see all books\n6.select Book\n7.exit\n")
    op=int(input("enter the option from above menue: "))
    match (op):
        case 1:
            current=Book()
            current.details()
            books.append(current)
            print("Details added successfully")
        case 2:
            if current is None:
                print("please add a book first")
            else:
                current.print_details()
                print()
            
        case 3:
            if current is None:
                print("please enter the book details")
            else:
                current.issue()
        case 4:
            if current is None:
                print("please enter book details")
            else:
                current.ret()
        case 5:
            if not books:
                print("please enter book details")
            else:
                print("---------ALL BOOKS----------")
                for i in books:
                    print(f"{i}\n")
        case 6:
            for i,book in enumerate(books,start=1):
                print(f"{i}. {book}")
            s=int(input("select book you want to modify:"))
            if 0<s<=len(books):
                current=books[s-1]
            else:
                print("enter valid book number")
        
        case 7:
            print("........YOU ARE EXITING..........")
            break
        case _:
            print("please enter the valid option")
            
            
        

            

        

