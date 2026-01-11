import os.path
import sys
from stats import word_count, get_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
# Returns filepath as string

def main():
    book_path = sys.argv[1]

    # Beginning Bookbot
    print(f"============ BOOKBOT ============")

    text = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")
    # Taking bookpath and beginning analysis

    print(f"----------- Word Count ----------")
    # Bookpath text word count tallied
    num_words = word_count(text)
    print(f"Found {num_words} total words")

    #Starting Character count
    print(f"--------- Character Count -------")

    # Bookpath text character count tallied in dictionary and sorted
    characters = get_char_counts(text)
    character_count_string = ""
    character_count_keys = characters.keys()
    for key in character_count_keys:
        if not key.isalpha():
            continue
        character_count_string += key + ": " + str(characters[key]) + f'\n'
    print(character_count_string, end="")
    # Sys arguments
if __name__== '__main__':
    if not len(sys.argv) == 2:
        print(f'Usage: python3 {sys.argv[0]} <path_to_book>')
        sys.exit(1)
    if not os.path.isfile(sys.argv[1]):
        print("Error: File does not exist")
        sys.exit(1)
    # End of bookbot analysis
    print(f"============= END ===============")
main()


