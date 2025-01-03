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

def main():
    file_contents = elab_file("books/frankestein.txt")
    words = word_count(file_contents)
    print(f"number of words in Frankenstein: {words}")
    
    print(f"----------------------------------------------------")
    print(f"Letter rank in Frankenstein")
    ranks = {}
    ranks = letters_ranking(file_contents)
    print(f"{ranks}")
main()