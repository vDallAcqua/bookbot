from stats import get_num_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        return f.read()
        

def main():
    file_contents = get_book_text('./books/frankenstein.txt')
    # #1 objective: print(file_contents)
    words = count_words(file_contents)
    print(f"{words} words found in the document")

main()