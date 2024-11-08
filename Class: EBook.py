class EBook:
    def __init__(self, title, author, publication_date, genre, price, isbn):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.genre = genre
        self.price = price
        self.isbn = isbn

    def __str__(self):
        return "Title: " + self.title + ", Author: " + self.author + ", Price: " + str(self.price)
