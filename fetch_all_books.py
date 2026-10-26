"""Read all books from the Book API, 10 books at a time.

Usage:
    python fetch_all_books.py [BASE_URL]

BASE_URL defaults to http://localhost:5000. To use the app running in Codio,
pass its URL, e.g. https://<your-box>-5000.codio.io
"""
import json
import sys
import urllib.request


LIMIT = 10


def fetch_page(base_url, page, limit=LIMIT):
    url = f"{base_url}/api/books?page={page}&limit={limit}"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_all_books(base_url):
    all_books = []
    page = 1
    while True:
        books = fetch_page(base_url, page)
        print(f"Page {page}: got {len(books)} books")
        all_books.extend(books)
        if len(books) < LIMIT:
            break
        page += 1
    return all_books


if __name__ == "__main__":
    base_url = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "http://localhost:5000"
    books = fetch_all_books(base_url)
    print(f"Fetched {len(books)} books in total")
