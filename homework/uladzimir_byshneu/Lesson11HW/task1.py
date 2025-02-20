class Book:
    material = 'бумага'
    text = True

    def __init__(self, book_title, author, number_pages, isbn, book_reservation):
        self.book_title = book_title
        self.author = author
        self.number_pages = number_pages
        self.isbn = isbn
        self.book_reservation = book_reservation


book_1 = Book('Атлант расправил плечи', "А.Рэнд", 1408, 'ISBN 978-5-9614-6742-0', True)
book_2 = Book('Empire V', 'В. Пелевин', 267, 'ISBN 978-5-389-10814-1', False)
book_3 = Book('Отцы и дети', 'И. Тургенев', 400, 'ISBN 978-5-17-089255-6', True)
book_4 = Book("Герой нашего времени", "М. Лермонтов", 333, 'ISBN 978-5-389-24394-1', True)
book_5 = Book("Жизнь взаймы", "Э. Ремарк", 245, 'ISBN 978-5-17-112096-2', False)

books = []
books.append(book_1)
books.append(book_2)
books.append(book_3)
books.append(book_4)
books.append(book_5)

for book in books:
    print('Название:', book.book_title + ',', 'Автор:', book.author + ',', 'страниц:',
          str(book.number_pages) + ',', 'материал:', book.material + ', зарезервирована'
          if book.book_reservation is True else book.material)


class SchoolBook(Book):

    def __init__(self, title, author, number_pages, isbn, book_reservation,
                 subject, school_class, task_available):
        super().__init__(title, author, number_pages, isbn, book_reservation)
        self.subject = subject
        self.school_class = school_class
        self.task_available = task_available


guide_1 = SchoolBook('Химия 9-й класс', 'Гурченко', 345, '', True, 'Химия', '9', True)
guide_2 = SchoolBook('Русская литература 7-й класс', 'Пушкин', 368, '', False, 'Русская литература', '7', True)
guide_3 = SchoolBook('Английский язык 8-й класс', 'Микашевич', 140, '', False, 'Иностранный язык', '8', True)

guides = []
guides.append(guide_1)
guides.append(guide_2)
guides.append(guide_3)

for guide in guides:
    print('Название:', guide.book_title + ',', 'Автор:', guide.author + ',', 'страниц:',
          str(guide.number_pages) + ',', 'предмет:', guide.subject + ',', 'класс:',
          guide.school_class + ', зарезервирована' if guide.book_reservation is True else guide.school_class)
