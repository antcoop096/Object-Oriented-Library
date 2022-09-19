from Book import Book
from Library import Library

#STEP 1---------------------------------------

# Small test of the Book class
example = Book()
example.setTitle("Harry Potter")
print("Title (Harry Potter): " + example.getTitle())

example.get_borrowed()

print("Borrowed? (should be false): " + example.isBorrowed())

example.get_rented()

print("Borrowed? (should be true): " + example.isBorrowed())

example.get_returned()

print("Borrowed? (should be false): " + example.isBorrowed())

#Step 2 ------------------------------------------
firstLibrary = Library()
secondLibrary = Library()
firstLibrary.setAddress("10 Main St.")
secondLibrary.setAddress("228 Liberty St.")

#Add four books to the first library
The_Lord_of_the_Rings = Book()
The_Lord_of_the_Rings.setTitle("The Lord of the Rings")

The_Da_Vinci_Code = Book()
The_Da_Vinci_Code.setTitle("The Da Vinci Code")

A_Tale_of_Two_Cities = Book()
A_Tale_of_Two_Cities.setTitle("A Tale of Two Cities")

Le_Petit_Prince = Book()
Le_Petit_Prince.setTitle("Le Petit Prince")

firstLibrary.addBook(The_Lord_of_the_Rings)
firstLibrary.addBook(The_Da_Vinci_Code)
firstLibrary.addBook(A_Tale_of_Two_Cities)
firstLibrary.addBook(Le_Petit_Prince)


#Print opening hours and the addresses
firstLibrary.setOpeningHours("7:00AM - 7:00PM")
print("Library hours:")
firstLibrary.printOpeningHours()
print()
print("Library addresses:")
firstLibrary.printAddress()
secondLibrary.printAddress()
print()

#Try to borrow The Lords of the Rings from both libraries
your_book_collection = []
print("Borrowing The Lord of the Rings:")
firstLibrary.borrowBook(The_Lord_of_the_Rings, your_book_collection)
secondLibrary.borrowBook(The_Lord_of_the_Rings, your_book_collection)
print()

#Print the titles of all available books from both libraries
print("Books available in the first library:")
firstLibrary.printAvailableBooks()
print()
print("Books available in the second library:")
secondLibrary.printAvailableBooks()
print()

#Return The Lords of the Rings to the first library
print("Returning The Lord of the Rings:")
firstLibrary.returnBook(The_Lord_of_the_Rings,your_book_collection)
print()

#Print the titles of available from the first library
print("Books available in the first library:")
firstLibrary.printAvailableBooks()

#PICKING UP: finish hours part