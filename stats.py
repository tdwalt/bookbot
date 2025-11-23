def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    stats = {}
    for char in text:
        if not char.isalpha():
            continue
        lower = char.lower()
        if lower in stats:
            stats[lower] += 1
        else:
            stats[lower] = 1
    return stats

def sort_chars(chars):
    def sort_on(items):
        return items["num"]
    char_list = []
    for char in chars:
        char_list.append({"char": char, "num": chars[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list