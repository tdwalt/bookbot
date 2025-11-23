from stats import count_words
from stats import count_chars
from stats import sort_chars
import sys

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    wc = count_words(text)
    output = f"Found {wc} total words"
    print("----------- Word Count ----------")
    print(output)
    char_count = count_chars(text)
    char_sorted = sort_chars(char_count)
    print("--------- Character Count -------")
    for char in char_sorted:
        print(f"{char["char"]}: {char["num"]}")
main()