from stats import word_count, get_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
# Returns filepath as string

def main():
    book_path = "books/frankenstein.txt"

    # Beginning Bookbot
    print(f"============ BOOKBOT ============")

    text = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")
    # Taking bookpath and beginning analysis

    print(f"----------- Word Count ----------")
    # Bookpath text word count tallied
    num_words = word_count(text)
    print(f"Found {num_words} total words")

    # Bookpath text character count tallied
    characters = get_char_counts(text)
    print(characters)

main()


