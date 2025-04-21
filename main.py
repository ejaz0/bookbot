from stats import books_number_words

def get_books_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_path = './books/frankenstein.txt'
    text = get_books_text(book_path)
    num_words = books_number_words(text)
    print(f"{num_words} words found in the document")
main()