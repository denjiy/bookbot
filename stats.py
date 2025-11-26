def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    return len(book.split())

def count_letters(book):
    letters = {}
    for letter in book:
        letter = letter.lower()
        if letter.isalpha():
            if letter not in letters:
                letters[letter]=1
            else:
                letters[letter]+=1
    return letters

def sort_dict(dict):
    return sorted(dict.items(), key=lambda item: item[1],reverse=True)

