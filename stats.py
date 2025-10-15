import re
#from main import get_book_text

def count_words(book_text):
    num_words = 0
    words = book_text.split()
    for word in words:
        num_words+= 1
    #print(f'Found {num_words} total words')
    return num_words


    
def count_letters(book_text):

    words_trimmed  = [ch.lower() for ch in book_text if ch.isalpha()]
    abc_dict = {}
    
    for letter in words_trimmed:    
        if letter in abc_dict:# and letter.isalpha():
                abc_dict[letter] += 1
        else:
        #elif letter.isalpha():
            abc_dict[letter] = 1

    return abc_dict

def sort_on(item):
     return item["num"]

def sorted_dictinary_lists(dict):
    list = []
    for item in dict:
        mini_dict = {
            "char": item, "num" : dict[item]
        }
        list.append(mini_dict)
    list.sort(reverse=True, key=sort_on)
    #print(list)
    return list


    


