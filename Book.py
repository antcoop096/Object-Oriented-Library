class Book:

  #Creates a new Book
  def __init__(self):
    self.title = None
    self.borrowed = None 
    
  #Sets title
  def setTitle(self,new_title):
   #Implement this method
   self.title = new_title

  def printTitle(self):
   print(self.title)

  #Marks the book as rented
  def get_borrowed(self):
  #Implement this method
   self.borrowed = 'False'

  #Marks the book as rented
  def get_rented(self):
   #Implement this method
   self.borrowed = 'True'
  
  #Marks the book as not rented
  def get_returned(self):
  #Implement this method
   self.borrowed = 'False'
    
  #Returns true if the book is rented, false otherwise
  def isBorrowed(self):
    #Implement this method
   return self.borrowed
  #Returns the title of the book
  def getTitle(self):
   #Implement this method
   return self.title

#PICKING UP: Figure out why replit is saying that it dosent have a get_rented attribute