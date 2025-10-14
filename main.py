from stats import count_words

def get_book_text(path_to_file):
    book_content = ""
    with open (path_to_file) as f:
        book_content = f.read()
    return book_content
#Write a new function that accepts the text from the book as a string, and returns 
# the number of words in the string. The .split() method will be belpful here.


def main():
    path = "books/frankenstein.txt"
    count_words(get_book_text(path))
    #print(get_book_text(path))



main()

    