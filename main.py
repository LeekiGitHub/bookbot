import sys
from stats import count_words, count_characters, sort_characters

USAGE = "Usage: python3 main.py <path_to_book>"

def get_book_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print(USAGE)
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)

    word_count = count_words(book_text)
    sorted_chars = sort_characters(count_characters(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
