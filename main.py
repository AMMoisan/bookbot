from stats import get_book_text
from stats import word_counter

def main():
    filepath = 'books/frankenstein.txt'
    #print(get_book_text(filepath))
    print(f'Found {word_counter(filepath)} total words')


main()

