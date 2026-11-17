import csv
from pathlib import Path
from .models import Author, Book

FIELDS = ["genre","first_name","middle_name","last_name","date_of_birth","title","published_year","price","quantity","isbn"]

class InventoryRepository:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self._write([])

    def all(self):
        books=[]
        with self.path.open(newline="", encoding="utf-8") as file:
            reader=csv.DictReader(file)
            for line, row in enumerate(reader, start=2):
                try:
                    author=Author(row["first_name"],row["last_name"],row.get("middle_name",""),row.get("date_of_birth",""))
                    books.append(Book(row["genre"],row["title"],author,int(row["published_year"]),float(row["price"]),int(row["quantity"]),row["isbn"]))
                except (ValueError, TypeError, KeyError) as exc:
                    raise ValueError(f"Invalid inventory data on CSV line {line}: {exc}") from exc
        return books

    def _write(self, books):
        with self.path.open("w", newline="", encoding="utf-8") as file:
            writer=csv.DictWriter(file,fieldnames=FIELDS)
            writer.writeheader()
            for b in books:
                writer.writerow({
                    "genre":b.genre,"first_name":b.author.first_name,"middle_name":b.author.middle_name,
                    "last_name":b.author.last_name,"date_of_birth":b.author.date_of_birth,
                    "title":b.title,"published_year":b.published_year,"price":f"{b.price:.2f}",
                    "quantity":b.quantity,"isbn":b.isbn
                })

    def add(self, book):
        books=self.all()
        if any(existing.isbn == book.isbn for existing in books):
            raise ValueError("A book with that ISBN already exists.")
        books.append(book); self._write(books)

    def update_quantity(self, isbn, quantity):
        if quantity < 0: raise ValueError("Quantity cannot be negative.")
        books=self.all(); found=False
        for book in books:
            if book.isbn == isbn:
                book.quantity=quantity; found=True; break
        if not found: raise ValueError("No book found with that ISBN.")
        self._write(books)

    def delete(self, isbn):
        books=self.all(); remaining=[b for b in books if b.isbn != isbn]
        if len(remaining)==len(books): raise ValueError("No book found with that ISBN.")
        self._write(remaining)
