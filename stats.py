import re

def count_words(book_text):
    num_words = 0
    words = book_text.split()
    for word in words:
        num_words+= 1
    print(f'Found {num_words} total words')

def count_letters(book_text):
    abc_dict = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
    words_trimmed  = re.sub(r'[^a-zA-Z]', '', book_text)

    
    for letter in words_trimmed:
        abc ='abcdefghijklmnopqrstuvwxyz' 
        for letter_abc in abc:
            if letter_abc.lower() == letter.lower():
                abc_dict[letter.lower()] += 1
       #print(f'{letter}: {abc_dict[letter.lower()]}')
    for letter in abc_dict :
       print(f"'{letter}': {abc_dict[letter.lower()]}")
