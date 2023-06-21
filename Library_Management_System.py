class Library:
    
    def __init__(self, bookList):
        self.books = bookList


    def availableBooks(self):
        for index,i in enumerate(self.books):
            print(str(index+1)+". ",i)

    
    def issueBook(self, bookname):
        if bookname in self.books:
            print(f"{bookname} issued.")
            self.books.remove(bookname)
        else:
            print("Book not available.")


    def returnBook(self,bookname):
        if bookname in self.books:
            print("Already available...")
        else:
            self.books.append(bookname)
            print(f"{bookname} available.")


class Student:

    def reqBook(self):
        issue = input("Enter book number to be issued: ")
        return issue
    
    def retBook(self):
        ret = input("Enter book to be returned: ")
        return ret



if __name__ == "__main__":

    l = Library(["Python","AIR","Big Data","Computer Vision","Deep Learning"])
    s = Student()


    while True:
        print("Choose from the following options: ")
        print('''
        1. Display the list of books available.
        2. Issue a book
        3. Return a book
        4. Quit
        ''')

        user = int(input("Enter your choice: "))
        if user == 1:
            l.availableBooks()
        elif user == 2:
            issue = s.reqBook()
            l.issueBook(issue)
        elif user == 3:
            ret = s.retBook()
            l.returnBook(ret)
        elif user == 4:
            exit()
        else:
            print("Enter valid choice..")




