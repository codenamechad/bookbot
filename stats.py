def count_words(text):
    words = text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def count_chars(text):
    lower_text = text.lower()
    char_counts = {}
    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(items):
    return items["num"]

def sort_chars(dict):
    char_list = []
    for char, count in dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

