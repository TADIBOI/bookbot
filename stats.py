def count_words(book_text):
    num_words = 0
    words = book_text.split()
    for word in words:
        num_words+= 1
    print(f'Found {num_words} total words')
