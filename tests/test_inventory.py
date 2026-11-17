import tempfile
import unittest
from pathlib import Path
from aggie_bookstore.models import Author, Book
from aggie_bookstore.repository import InventoryRepository
from aggie_bookstore.services import summarize_inventory, search_books

class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.repo=InventoryRepository(Path(self.temp.name)/"inventory.csv")
        self.book=Book("Fiction","Dune",Author("Frank","Herbert"),1965,15.50,3,"ISBN-1")
    def tearDown(self): self.temp.cleanup()
    def test_add_and_read(self):
        self.repo.add(self.book)
        self.assertEqual(self.repo.all()[0].title,"Dune")
    def test_duplicate_isbn_rejected(self):
        self.repo.add(self.book)
        with self.assertRaises(ValueError): self.repo.add(self.book)
    def test_update_quantity(self):
        self.repo.add(self.book); self.repo.update_quantity("ISBN-1",8)
        self.assertEqual(self.repo.all()[0].quantity,8)
    def test_delete(self):
        self.repo.add(self.book); self.repo.delete("ISBN-1")
        self.assertEqual(self.repo.all(),[])
    def test_summary_uses_quantity_times_price(self):
        self.repo.add(self.book)
        result=summarize_inventory(self.repo.all())
        self.assertEqual(result["Fiction"]["copies"],3)
        self.assertEqual(result["Fiction"]["value"],46.5)
    def test_search(self):
        self.repo.add(self.book)
        self.assertEqual(len(search_books(self.repo.all(),"herb")),1)
    def test_negative_quantity_rejected(self):
        with self.assertRaises(ValueError):
            Book("Fiction","Dune",Author("Frank","Herbert"),1965,15.5,-1,"ISBN-1")

if __name__=="__main__": unittest.main()
