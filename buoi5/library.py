class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_borrowed = False

    @property
    def is_borrowed(self):
        return self._is_borrowed

    def borrow(self):
        if self._is_borrowed:
            return False
        else:
            self._is_borrowed = True
            return True

    def return_book(self):
        if self._is_borrowed== True:
            self._is_borrowed = False
            return True
        else:
            return False

    def describe(self):
        if self._is_borrowed:
            status = "Da duoc muon"
        else:
            status = "Chua duoc muon"
        return f"Ten sach: {self.title}, Tac gia: {self.author}"


book1 = Book("De Men Phieu Luu Ky", "To Hoai")
book2 = Book("Tat Den", "Ngo Tat To")

print(book1.describe())
print(book2.describe())

print("Muon book1 lan 1:", book1.borrow())
print("Muon book1 lan 2:", book1.borrow())
print("Trang thai book1:", book1.is_borrowed)
print(book1.describe())

printf("Tra book1 lan 1:", book1.return_book())
print("Trang thai book1:", book1.is_borrowed)
print(book1.describe())

print("Tra book2 khi chua muon:", book2.return_book())
print("Muon book2:", book2.borrow())
print(book2.describe())