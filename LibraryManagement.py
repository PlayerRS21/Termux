import json

class Library:
    books={}
    no_of_books=0
    BookName=""
    BookPublisher=""
    PublishedYear=0

    def checkNumOfBooks(self):
        if self.no_of_books!=len(self.books):
           #print("Error in Number of books\nFixing Error...\nError Fixed")
            self.no_of_books=len(self.books)

    def loadData(self):
        with open("books.json","r") as f:
            self.books=json.load(f)

    def __init__(self):
        #print("Loading...")
        self.loadData()
        self.checkNumOfBooks()

    def saveData(self):
        with open("books.json","w") as f:
            txt=json.dumps(self.books, indent=4)
            f.write(txt)
            print("Data Saved")

    #def loadData(self):
        #with open("books.json","r") as f:
            #books= json.loads(f)
    
    def addBook(self):
        name=input("Enter Name Of Book:\n")         
        #author=input("Enter Writer Of the Book:\n") 
        #p_year=input("Enter Publication Year:\n")   
        #shelf=input("Enter shelf number: \n")       
        #row=input("Enter row number:\n")

        if name in self.books:
            isBorrowed=input("Is this book returned from a borrower: ")
            if isBorrowed.lower()=="y":
                borrowerNumber=input("Enter Borrower Number: ")
                shelf=input("Enter shelf number: \n")
                row=input("Enter row number:\n")
                self.books[name]["inStore"]=True
                self.books[name].pop("to")
                self.books[name]["location"]=f"Shelf :{shelf}, Row: {row}"
                print("Saving Data")
                input("")
        else:
            author=input("Enter Writer Of the Book:\n")
            p_year=input("Enter Publication Year:\n")
            shelf=input("Enter shelf number: \n")
            row=input("Enter row number:\n")

            self.books[name]={"BookName":name,"Author":author,"Year of Publishtion":p_year,"inStore":True,"location":f"Shelf: {shelf}, Row: {row}"}

            #self.addNew()          

        #self.BookName=name
        #self.BookPublisher=author
        #self.PublishedYear=p_year
        #def addNew(self):
            #self.books[name]={"BookName":name,"Author":author,"Year of Publishtion":p_year,"inStore":True,"location":f"Shelf: {shelf}, Row: {row}"}

        print("\n\nDone")
        self.saveData()
        input("")

    def fetchBook(self,name):
        for i in self.books:
            if i.lower()==name.lower():
                print("Book Found")
                print(self.books[i]["BookName"])
                print("Location  ",self.books[i]["location"])
                input("")
                break
        else:
            print("Book Not Found")
            input("")

    def lendBook(self,name,pName,mNumber):
        self.books[name]["inStore"]=False
        self.books[name]["to"]={"Person":pName,"MNumber":mNumber}
        self.saveData()
        print("Done")
        input("")

    def listAllBooks(self):
        if len(self.books)!=0:
            for i in self.books:
                if self.books[i]["inStore"]==True:
                    print(self.books[i]["BookName"])
            else:
                input("")
        else:
            print("No Books Found.")
            input("")

    def listLendBooks(self):
        if len(self.books)!=0:
            for i in self.books:
                if self.books[i]["inStore"]==False:
                    print(f"{self.books[i]["BookName"]}:\n\tLended to: {self.books[i]["to"]["Person"]}\n\tMobile Number:{self.books[i]["to"]["MNumber"]}")
            else:
                input("")
        else:
            print("No Books Found.")
            input("")
    
    def numOfBooks(self):
        x=0
        for i in self.books:
            if self.books[i]["inStore"]==True:
                x+=1
        print("Total Number Of Books: ",x)
        input("")

ex=False
b=Library()
while (ex==False):
    print("""

    """)
    a=input("What you want to do\n1. Add Book (1)\n2. List All Books (2)\n3. Find Book (3)\n4. Lend Book (4)\n5. Find Number Of Books (5) \n6. List Lended Books (6) \n7. Exit (e) \n--> ")

    print("""


      """)

    if (a.lower()=="e"):
        ex=True
        break
    elif (a=="1"):
        #x=input("Enter Name Of Book:\n")
        #y=input("Enter Writer Of the Book:\n")
        #z=input("Enter Publication Year:\n")
        #s=input("Enter shelf number: \n")
        #r=input("Enter row number:\n")

        b.addBook()
    elif (a=="2"):
        b.loadData()
        b.listAllBooks()
    elif (a=="3"):
        n=input("Enter Book Name You Want To Search: ")
        b.fetchBook(n)
    elif (a=="4"):
        n=input("Enter the exact book you want to remove(case-sensitive): ")
        if n in b.books:
            c=input("Enter the borrower name: ")
            m=int(input("Enter Mobile Number of Borrower: "))
            b.lendBook(n,c,m)

        else:
            print("Book Not Found")
    elif (a=="5"):
        b.numOfBooks()
    elif (a=="6"):
        b.loadData()
        b.listLendBooks()
    else:
        print("Wrong Input")


print("Thanks For using the app.")
