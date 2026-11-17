from collections import defaultdict
from .models import Author, Book
from .services import summarize_inventory, search_books

def _ask_int(prompt, minimum=0):
    while True:
        try:
            value=int(input(prompt))
            if value < minimum: raise ValueError
            return value
        except ValueError:
            print(f"Enter a whole number greater than or equal to {minimum}.")

def _ask_float(prompt, minimum=0):
    while True:
        try:
            value=float(input(prompt))
            if value < minimum: raise ValueError
            return value
        except ValueError:
            print(f"Enter a number greater than or equal to {minimum}.")

def show_books(books):
    if not books:
        print("No books found."); return
    print(f"{'Genre':<18} {'Title':<30} {'Author':<24} {'Year':>6} {'Qty':>5} {'Price':>10} {'ISBN'}")
    print("-"*116)
    for b in books:
        print(f"{b.genre[:17]:<18} {b.title[:29]:<30} {b.author.full_name[:23]:<24} {b.published_year:>6} {b.quantity:>5} ${b.price:>9.2f} {b.isbn}")

def run(repo):
    print("\nWelcome to Aggie Bookstore Inventory Manager")
    while True:
        print("\n1. View all books\n2. Browse by genre\n3. Search books\n4. Add a book\n5. Update quantity\n6. Delete a book\n7. Inventory summary\n8. Exit")
        choice=input("Choose an option: ").strip()
        try:
            books=repo.all()
            if choice=="1": show_books(books)
            elif choice=="2":
                genres=sorted({b.genre for b in books})
                if not genres: print("No genres available."); continue
                for i,g in enumerate(genres,1): print(f"{i}. {g}")
                raw=input("Select genre: ").strip()
                if raw.isdigit() and 1<=int(raw)<=len(genres): show_books([b for b in books if b.genre==genres[int(raw)-1]])
                else: print("Invalid genre selection.")
            elif choice=="3": show_books(search_books(books,input("Search title, author, or ISBN: ")))
            elif choice=="4":
                genre=input("Genre: ").strip(); title=input("Title: ").strip()
                author=Author(input("Author first name: ").strip(),input("Author last name: ").strip(),input("Author middle name (optional): ").strip(),input("Author date of birth (optional): ").strip())
                year=_ask_int("Publication year: "); price=_ask_float("Price: "); qty=_ask_int("Quantity: "); isbn=input("ISBN: ").strip()
                repo.add(Book(genre,title,author,year,price,qty,isbn)); print("Book added.")
            elif choice=="5": repo.update_quantity(input("ISBN: ").strip(),_ask_int("New quantity: ")); print("Quantity updated.")
            elif choice=="6": repo.delete(input("ISBN to delete: ").strip()); print("Book deleted.")
            elif choice=="7":
                summary=summarize_inventory(books)
                if not summary: print("Inventory is empty.")
                for genre, values in summary.items():
                    print(f"{genre}: {values['titles']} titles | {values['copies']} copies | Inventory value ${values['value']:.2f}")
                print(f"TOTAL: {sum(v['copies'] for v in summary.values())} copies | ${sum(v['value'] for v in summary.values()):.2f}")
            elif choice=="8": print("Thank you for using Aggie Bookstore. Goodbye!"); break
            else: print("Please choose an option from 1 to 8.")
        except (ValueError, OSError) as exc:
            print(f"Unable to complete request: {exc}")
