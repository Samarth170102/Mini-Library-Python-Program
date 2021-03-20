class Library:

    books = ['BookA', 'BookB', 'BookC', 'BookD',
             'BookE', 'BookF', 'BookG', 'BookH']

    lend_books = []

    @classmethod
    def display(cls):
        """Function to show the name of the library books"""

        i = 0
        for item in cls.books:
            i += 1
            print(i, item)

    @classmethod
    def add_book(cls, name):
        """Function to add a new book to the library"""

        cls.books.append(name)

    @classmethod
    def lend_book(cls, name):
        """Function to lend the book from the library"""

        cls.lend_books.append(name)
        cls.books.remove(name)

    @classmethod
    def return_book(cls, value, name):
        """Function to return the book which was lend from the library"""

        if name in cls.books:
            print("\nThe book already exist in library\n")
        else:
            cls.lend_books.remove(name)
            cls.books.insert(value, name)
          
    @classmethod
    def display_lend_books(cls):
        """Function to display the books which were landed"""

        if cls.lend_books == []:
            print("\nThere are no books which are lended")
        else:  
            for item in cls.lend_books:       
                print(item)


if __name__ == '__main__':

    value = int
    name = str
    ask = str

    name = Library()

    while True:

        ask = input("\nWhat you want to do?\n\n"
                    'Display the books\nAdd the book\nLend the book\nReturn the lend book'
                    '\nSee the lend books\nRemove from the program\n\n')

        if ask == 'Display the books':

            Library.display()

        elif ask == 'Add the book':

            name = input("Enter the book name: ")
            Library.add_book(name)

        elif ask == 'Lend the book':

            Library.display()
            name = input("Which book you want to lend: ")
            Library.lend_book(name)

        elif ask == 'Return the lend book':

            name = input("Which book you want to return?: ")
            value = int(input("Where you want to put that book?: "))
            Library.return_book(value - 1, name)

        elif ask == 'See the lend books':
            Library.display_lend_books()
            
        elif ask == 'Remove from the program':

            print("Thank you for using my library program")
            break