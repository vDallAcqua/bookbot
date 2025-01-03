def elab_file(path):
    with open(path) as f:
        return f.read()
        
def word_count(text):
    words = []
    words = text.split()
    return len(words)

def letters_ranking(text):
    lowered = text.lower()
    ranks = {}
    for i in range(0, len(lowered)):
        char = lowered[i]
        rank_letter = ranks.get(char)
        if rank_letter == None:
            ranks[char] = 1
        else:
            ranks.update({char: rank_letter + 1})
    return ranks

def sort_on(list):
    return list[0]

def print_report_dict(ranks):
    letters = []
    letters = list(ranks.items())
    letters.sort(reverse=False, key=sort_on)
    for letter in letters:
        if letter[0].isalpha():
            print(f"The {letter[0]} character was found {letter[1]} times")

def main():
    file_contents = elab_file("books/frankestein.txt")
    words = word_count(file_contents)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    
    ranks = {}
    ranks = letters_ranking(file_contents)
    print_report_dict(ranks)
main()