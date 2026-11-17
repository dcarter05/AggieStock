# Aggie Stock | Inventory Management System

A Python-based inventory management system designed to organize and manage bookstore inventory. The application uses object-oriented programming and CSV file storage to support book management, inventory tracking and automated reporting.

## Features

- **Inventory Management:** Add, update, delete and view bookstore inventory.
- **Book Search:** Search for books by title, author or ISBN.
- **CSV Data Storage:** Read and write inventory records using CSV files.
- **Input Validation:** Validate book information and prevent duplicate ISBN entries.
- **Inventory Reporting:** Calculate stock quantities and inventory value by genre.
- **Automated Testing:** Unit tests to verify core application functionality.

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- CSV File Processing
- Unit Testing (`unittest`)

## Project Structure

```text
AggieBookstore/
│
├── data/
│   └── inventory.csv
│
├── tests/
│   └── test_inventory.py
│
├── main.py
├── book.py
├── inventory.py
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.9 or later
- PyCharm or another Python IDE

### Installation

1. Clone the repository:

```bash
git clone https://github.com/dcarter05/AggieBookstore.git
```

2. Navigate into the project directory:

```bash
cd AggieBookstore
```

3. Run the application:

```bash
python main.py
```

## Running Tests

Run the automated unit tests with:

```bash
python -m unittest discover -s tests -v
```

## Purpose

Aggie Stock was developed to strengthen my Python programming skills through practical application of object-oriented programming, data management and software testing. The project demonstrates how programming can improve inventory organization and streamline bookstore operations.

## Author

**Dorian Carter**

Business Information Technology Student  
North Carolina A&T State University

- [GitHub](https://github.com/dcarter05)
- [LinkedIn](https://www.linkedin.com/in/dorian-l-carter/)
