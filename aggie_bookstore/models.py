from dataclasses import dataclass

@dataclass
class Author:
    first_name: str
    last_name: str
    middle_name: str = ""
    date_of_birth: str = ""

    @property
    def full_name(self) -> str:
        return " ".join(part for part in (self.first_name, self.middle_name, self.last_name) if part).strip()

@dataclass
class Book:
    genre: str
    title: str
    author: Author
    published_year: int
    price: float
    quantity: int
    isbn: str

    def __post_init__(self):
        self.genre = self.genre.strip()
        self.title = self.title.strip()
        self.isbn = self.isbn.strip()
        if not self.genre or not self.title:
            raise ValueError("Genre and title are required.")
        if self.published_year < 0:
            raise ValueError("Published year cannot be negative.")
        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative.")

    @property
    def inventory_value(self) -> float:
        return round(self.price * self.quantity, 2)
