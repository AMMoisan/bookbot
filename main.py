from stats import get_book_text, word_counter, char_counter

def main():
    filepath = 'books/frankenstein.txt'
    #print(get_book_text(filepath))
    print(f'Found {word_counter(filepath)} total words')
    print(char_counter(filepath))


main()

