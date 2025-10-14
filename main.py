def get_book_text(path_to_file):
    book_content = ""
    with open (path_to_file) as f:
        book_content = f.read()
    return book_content

def main():
    path = "books/frankenstein.txt"
    print(get_book_text(path))


main()

    