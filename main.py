from stats import count_words, count_everything, char_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

book_text = get_book_text(book_path)

word_count = count_words(book_text)
char_count_dict = count_everything(book_text)

sorted_list = char_list(char_count_dict)
sorted_list.sort(key=lambda x:x["num"], reverse=True)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for x in sorted_list:
    if x["char"].isalpha():
        print(f"{x["char"]}: {x["num"]}")
    else:
        pass
print("============= END ===============")

