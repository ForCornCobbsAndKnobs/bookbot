from stats import word_count, char_count, sort_char_count
import sys 
from sys import argv

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        file_contents = get_book_text(argv[1])
        word_count_total = word_count(file_contents)
        print(f"Analyzing book found at {argv[1]}...")
        char_count_totals = char_count(file_contents)
        sorted_char_count_totals = sort_char_count(char_count_totals)
        print("----------- Word Count ----------")
        print(f"Found {word_count_total} total words")
        print("------- Character Count --------")
        for char_count_dict in sorted_char_count_totals:
            print(f"{char_count_dict['char']}: {char_count_dict['num']}")
main()