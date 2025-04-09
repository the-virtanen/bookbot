from stats import get_num_words, get_num_characters, sort_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    
    character_count = get_num_characters(book_text)
    character_count = sort_characters(character_count)
    
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for c in character_count:
        print (f"{c[0]}: {c[1]}")
    print("============= END ===============")

main()
