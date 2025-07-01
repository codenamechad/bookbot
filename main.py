
import sys
from stats import count_words
from stats import count_chars
from stats import sort_chars


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    book_path = sys.argv[1] # set the path to be second  cli argument
    text = get_book_text(book_path) #get all the text from the second cli argument
    word_report = count_words(text) # counts total words
    char_count = count_chars(text) # returns a dictionary of chars and counts of them
    sorted_chars = sort_chars(char_count) # sorts based off sort function called on ^
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(word_report)
    print("--------- Character Count -------")
    for item in sorted_chars: # loop over the sorted dictionary and print according to format
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()



