def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_counter(filepath):
    text = get_book_text(filepath)
    words = text.split()
    return len(words)

        ## Testing fuckery to try and eliminate non-alphabetical characters
    #alphabet = ['A','a','B','b','C','c','D','d','E','e','F','f','G',
    #'g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p',
    #'Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
    #is_word == True

def char_counter(filepath):
    text = get_book_text(filepath)
    ltext = text.lower()
    unique_ch = []
    char_count = {}

    for char in ltext:
        if char not  in unique_ch:
            unique_ch.append(char)

    for ch in unique_ch:
        counter = 0
        for char in ltext:
            if ch == char:
                counter += 1
                char_count[ch] = counter

    return char_count