def get_num_words(content):
    content_words = content.split()
    return len(content_words)

def get_num_letters(content):
    letter_count = {}
    lower_content = content.lower()
    for char in lower_content:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count

def sort_letters_by_count(num_letters):
    sorted_occurrences = sorted(num_letters.items(), key=lambda item: item[1], reverse=True)
    return sorted_occurrences
