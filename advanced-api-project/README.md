# Advanced API Project – Generic Views Setup

## Views Implemented
- **BookListView** (`GET /books/`) – List all books.
- **BookDetailView** (`GET /books/<id>/`) – Retrieve a single book.
- **BookCreateView** (`POST /books/create/`) – Add a new book (Auth required).
- **BookUpdateView** (`PUT/PATCH /books/update/<id>/`) – Edit an existing book (Auth required).
- **BookDeleteView** (`DELETE /books/delete/<id>/`) – Remove a book (Auth required).

## Permissions
- Public Read Access for List & Detail views.
- Authenticated Write Access for Create, Update, and Delete.

## Filters
- List view supports optional `?title=` query param for searching by title.

## Testing
- Tested using Postman with both authenticated and unauthenticated requests.
- Verified permission restrictions for each view.

