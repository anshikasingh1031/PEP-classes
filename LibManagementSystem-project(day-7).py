#parent class-abstrcation
class LibraryItem:
    def __init__(self, item_id, title, borrow_days):
        self.item_id = item_id
        self.title = title
        self._borrow_days = borrow_days   # protected (Encapsulation)
    def calculate_charge(self):
        pass         # abstraction - implement by child 

#child class book  - inheritance 
class Book(LibraryItem):
    def __init__(self, item_id, title, borrow_days):
        super().__init__(item_id, title, borrow_days)
#polymorphism
    def calculate_charge(self):
        return self._borrow_days * 10   # book charge per day

# child class magazine - inheritance
class Magazine(LibraryItem):
    def __init__(self, item_id, title, borrow_days):
        super().__init__(item_id, title, borrow_days)
#polymorphism 
    def calculate_charge(self):
        return self._borrow_days * 10   # magazine charge per day
    #calculate charge diff using same method

# main class  - HAS-A relationship
class LibraryApp:
    def __init__(self):
        self.item = None   
    def create_item(self, item_type):
        if item_type == "Book":
            self.item = Book(1, "Python Basics", 5)
        else:
            self.item = Magazine(2, "Tech Weekly", 3)
        return "Item Created"
    def show_details(self):
        print("Item Type:", type(self.item).__name__)
        print("Borrow Days:", self.item._borrow_days)
        print("Borrowing Charge:", self.item.calculate_charge())
app = LibraryApp()
print(app.create_item("Book"))
app.show_details()

app2 = LibraryApp()
print(app2.create_item("Magazine"))
app2.show_details()
