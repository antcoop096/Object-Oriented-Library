from Book import Book

class Library:

  #Create libraries --> Does anything else need to be added to this function?
  def __init__(self):
    self.address = None
    self.hours = None
    self.books = []

  def setAddress(self,inputted_address):
    self.address = inputted_address

  def printAddress(self):
    print(self.address)
    
  def addBook(self,book):
   self.books.append(book)
    
  def printAvailableBooks(self):
   if len(self.books) > 0:
    for books in self.books:
     if books.printTitle() != None:
      print(books.printTitle())
   else: 
    print('There are no books in this library...')
  
  def setOpeningHours(self,inputted_hours):
   self.hours = inputted_hours
    
  def printOpeningHours(self):
   print(self.hours)

  def borrowBook(self,borrowed_book,list):
   if len(self.books) > 0:
    self.books.remove(borrowed_book)
    print("Borrow Successfull")
    list.append(borrowed_book)
   else:
     print("There are no books in this library...")

  def returnBook(self,borrowed_book,list):
   list.remove(borrowed_book)
   print("Return Successfull")
   self.books.append(borrowed_book)



  #Create the rest of the necessary functions below