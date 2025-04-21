from stats import books_number_words, num_of_characters, print_report
import sys

def get_books_text(path):
    with open(path) as f:
        return f.read()



def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_books_text(book_path)
        num_words = books_number_words(text)
        print(f"{num_words} words found in the document")
        num_chars = num_of_characters(text)
        print(num_chars)
        sorted_chars = print_report(num_chars)
        print("============ BOOKBOT ============")
        print(f"Analazying book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char_dict in sorted_chars:
            char = char_dict["char"]
            count = char_dict["count"]
            if char.isalpha():
                print(f"{char}: {count}")
        print("============= END ===============")



main()