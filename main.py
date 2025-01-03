def elab_file(path):
    with open(path) as f:
        return f.read()
        
def word_count(text):
    words = []
    words = text.split()
    return len(words)

def letters_ranking(text):
    ranks = {}
    for i in range(0, len(text)):
        char = text[i]
        rank_letter = ranks.get(char)
        if rank_letter == None:
            ranks[char] = 1
        else:
            ranks.update({char: rank_letter + 1})
    return ranks

def main():
    file_contents = elab_file("books/frankestein.txt")
    words = word_count(file_contents)
    print(f"number of words in Frankenstein: {words}")
    
    print("----------------------------------------------------")
    print("Letter rank in Frankenstein")
    ranks = {}
    ranks = letters_ranking(file_contents)
    print(ranks)
main()