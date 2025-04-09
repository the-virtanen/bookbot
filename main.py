from stats import get_num_words, get_num_characters, sort_characters
import sys

def main():
    book_path = select_book()
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    
    character_count = get_num_characters(book_text)
    character_count = sort_characters(character_count)
    
    print_report(book_path, word_count, character_count)

def select_book():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        print(sys.argv[0])
        print(sys.argv[1])
        return sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, word_count, character_count):
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for c in character_count:
        if c[0].isalpha():
            print (f"{c[0]}: {c[1]}")
    print("============= END ===============")

main()
