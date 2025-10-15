from stats import count_words
from stats import count_letters 
from stats import sorted_dictinary_lists

def get_book_text(path_to_file):
    book_content = ""
    with open (path_to_file) as f:
        book_content = f.read()
    return book_content
#Write a new function that accepts the text from the book as a string, and returns 
# the number of words in the string. The .split() method will be belpful here.
def print_stats(book_path):
    
    book_text = get_book_text(book_path)
    abc_dict = count_letters(book_text)
    sorted_list = sorted_dictinary_lists(abc_dict)
    num_words = count_words(book_text)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for letter in abc_dict :
        print(f"{letter}: {abc_dict[letter.lower()]}")


def main():
    path = "books/frankenstein.txt"
    #count_words(get_book_text(path))
    #count_letters(get_book_text(path))
    #print(get_book_text(path))
    print_stats(path)



main()

    