from stats import *

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(book_text)
    print(get_num_characters(book_text))
    
    #print(f"{word_count} words found in the document")

main()
