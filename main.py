from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    txt = get_book_text(filepath)
    num = num_words(txt)
    d = count_chars (txt)
    lst = report(d)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for i in lst:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
    

main()
