def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_counter(filepath):
    text = get_book_text(filepath)
    split = text.split()
    words = 0

    ## Testing fuckery to try and eliminate non-alphabetical characters
    #alphabet = ['A','a','B','b','C','c','D','d','E','e','F','f','G',
    #'g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p',
    #'Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
    #is_word == True

    for word in split:
        words += 1
    return words