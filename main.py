from stats import get_num_words
from stats import get_num_letters
from stats import sort_letters_by_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        return f.read()

def print_report(file_name, words, ord_letters):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    
    print("----------- Word Count ----------")    
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    for item in ord_letters:
        if (item[key]).isalpha():
            print(f"{item[key]}: {item[value]}")

def main():
    file_name = 'books/frankenstein.txt'
    file_contents = get_book_text(file_name)
    # #1 objective: print(file_contents)
    
    words = get_num_words(file_contents)
    
    num_letters = get_num_letters(file_contents)
    ord_letters = sort_letters_by_count(num_letters)
    print_report(file_name, words, ord_letters) 
    

main()