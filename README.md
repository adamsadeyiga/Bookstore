# Bookstore API

This is a simple Django project that provides an API for managing books and authors.
<br>Name: Bookstore
<br>Author: Adams Adeyiga

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/adamsadeyiga/Bookstore.git

2. Navigate to the project directory:
    ```bash
    cd bookstore

3. Create a virtual environment:
    ```bash
    python3 -m venv bookstoreEnv
4. Activate the virtual environment:
    ```bash 
    source bookstoreEnv/bin/activate

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

6. Apply the migrations:
    ```bash 
    python manage.py migrate

7. Run the development server:
    ```bash
    python manage.py runserver

## API Endpoints
### Authors
    GET /api/authors/ - List all authors
    POST /api/authors/ - Create a new author
    GET /api/authors/<id>/ - Retrieve a specific author
    PUT /api/authors/<id>/ - Update a specific author
    DELETE /api/authors/<id>/ - Delete a specific author
### Books
    GET /api/books/ - List all books
    POST /api/books/ - Create a new book
    GET /api/books/<id>/ - Retrieve a specific book
    PUT /api/books/<id>/ - Update a specific book
    DELETE /api/books/<id>/ - Delete a specific book