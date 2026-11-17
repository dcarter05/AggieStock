from collections import defaultdict

def summarize_inventory(books):
    summary=defaultdict(lambda: {"titles":0,"copies":0,"value":0.0})
    for book in books:
        group=summary[book.genre]
        group["titles"] += 1
        group["copies"] += book.quantity
        group["value"] += book.inventory_value
    for group in summary.values():
        group["value"]=round(group["value"],2)
    return dict(sorted(summary.items()))

def search_books(books, term):
    term=term.casefold().strip()
    return [b for b in books if term in b.title.casefold() or term in b.author.full_name.casefold() or term in b.isbn.casefold()]
