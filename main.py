from stats import get_book_text, word_counter, char_counter, itemize_dict
import sys

def main():

    if len(sys.argv) < 2:
        print("Please introduce 2 arguments. Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #print(get_book_text(filepath))
    #print(char_counter(filepath))

    print("============ BOOKBOT ============")
    filepath = sys.argv[1]

    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(filepath)} total words")
    print("--------- Character Count -------")

    item_list = itemize_dict(char_counter(filepath))
    def sort_on(items):
        return items["num"]

    item_list.sort(key=sort_on, reverse=True)

    for item in item_list:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()

