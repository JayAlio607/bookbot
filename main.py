import sys
from stats import get_num_words, get_num_unique_char, sort_unique_chars


def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
		return file_contents

def main():
	if len(sys.argv) == 2:
		path = sys.argv[1]
		book_text = get_book_text(path)
		num_words = get_num_words(book_text)
		unique_chars = get_num_unique_char(book_text)
		sorted_list = sort_unique_chars(unique_chars)
		print("============ BOOKBOT ============")
		print("Analyzing book found at " + path)
		print("----------- Word Count ----------")
		print("Found " + str(get_num_words(book_text)) + " total words")
		print("--------- Character Count -------")
		for item in sorted_list:
			if item["char"].isalpha():
				output = item["char"] + ": " + str(item["num"])
				print(output)
		print("============= END ===============")
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

main()
