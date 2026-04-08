# Level 1 — Basics Create a dictionary for a book with keys "title", author", and "year". Print each value using .items()


books = {
    "boo1": {"title": "Hello Book", "author": "Hey", "year": 2009, "rating": 4.5},
    "boo2": {"title": "Book B", "author": "Mr.B", "year": 2010, "rating": 4.0} 
}



for book in books.values():
    print(f"Title: {book['title']}, Year: {book['year']}")



# for key, value in book.items():
#     print(f"{key}: {value}")

# print(book.get("publisher", "unknown"))


# Level 2 — Safe accessn Add a "rating" key to your book dict. Then use .get() to safely fetch "publisher" (which doesn't exist) with a fallback of "Unknown".
# Level 3 — Nested Build a dict of 2 books, each identified by an ID like "b001", with the same fields inside. Write a loop that prints each book's title and year.
