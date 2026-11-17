from pathlib import Path
from aggie_bookstore.repository import InventoryRepository
from aggie_bookstore.cli import run

if __name__ == "__main__":
    data_file=Path(__file__).parent/"data"/"inventory.csv"
    run(InventoryRepository(data_file))
