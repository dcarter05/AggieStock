# Aggie Bookstore — Inventory Management System

A Python command-line inventory management application. The project uses object-oriented models and CSV persistence to organize bookstore titles, authors, stock quantities, and inventory value.

## Features
- Browse all inventory or filter by genre
- Search by title, author, or ISBN
- Add books with duplicate-ISBN protection
- Update stock quantities and delete records
- Calculate title counts, copy counts, and inventory value by genre
- Validate numeric input and inventory records
- Persist changes to a structured CSV file
- Automated unit tests for core inventory operations

## Requirements
- Python 3.9 or newer
- No third-party packages required

## Run
From the project folder:

```bash
python main.py
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

The included `data/inventory.csv` is a cleaned, header-based copy of the sample data supplied with the original project. The original source files are not required to run this version.
