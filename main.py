from stats import get_num_words
from stats import get_num_letters
from stats import sort_letters_by_count
import sys 

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        return f.read() 

def print_report(file_name, words, ord_letters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}")
    
    print("----------- Word Count ----------")    
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    for item in ord_letters:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    file_name = sys.argv[1]
    file_contents = get_book_text(file_name)
    # #1 objective: print(file_contents)
    
    words = get_num_words(file_contents)
    
    num_letters = get_num_letters(file_contents)
    ord_letters = sort_letters_by_count(num_letters)
    print_report(file_name, words, ord_letters) 
    

main()