from stats import get_book_text, word_counter, char_counter, itemize_dict

def main():
    #print(get_book_text(filepath))
    #print(char_counter(filepath))

    print("============ BOOKBOT ============")
    filepath = 'books/frankenstein.txt'

    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(filepath)} total words")
    print("--------- Character Count -------")

    item_list = itemize_dict(char_counter(filepath))
    def sort_on(items):
        return items["num"]

    item_list.sort(key=sort_on, reverse=True)

    for item in item_list:
        print(f"{item["char"]}:{item["num"]}")

    print("============= END ===============")

main()

