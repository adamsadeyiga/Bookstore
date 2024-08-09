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

## Example Usage
You can use tools like cURL or Postman to interact with the API. Here are some examples:

### List all authors:
```bash
    curl -X GET http://127.0.0.1:8000/api/authors/
```
### Create a new author:
```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Adams Adeyiga", "birth_date": "1980-01-01"}' http://127.0.0.1:8000/api/authors/
```
### Retrieve a specific author:
```bash
    curl -X GET http://127.0.0.1:8000/api/authors/1/
```
### Update a specific author:
```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name", "birth_date": "1980-01-01"}' http://127.0.0.1:8000/api/authors/1/
```
### Delete a specific author:
```bash
curl -X DELETE http://127.0.0.1:8000/api/authors/1/
```
## Additional API Endpoints for ORM Queries
### Books by a Specific Author

- **GET /api/books/by-author/\<author_id\>/** - List all books by a specific author

### Authors with at Least One Book

- **GET /api/authors/with-books/** - List all authors who have published at least one book

### Most Recent Book Published

- **GET /api/books/most-recent/** - Retrieve the most recent book published

# Enjoy!