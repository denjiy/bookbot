from stats import get_book_text, count_words, count_letters, sort_dict
import sys

def main():
    if (len(sys.argv)!=2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_words = count_words(book)
    letters = count_letters(book)
    sorted_letters = sort_dict(letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_letters:
        print(f"{c[0]}: {c[1]}")


main()