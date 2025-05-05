from stats import get_num_words
from stats import count_char

# Accept text from book as string and prints text
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
    print(file_contents)


def main():
    #get_book_text('books/frankenstein.txt')
    word_count = get_num_words('books/frankenstein.txt')
    character_count = count_char('books/frankenstein.txt')

    print(word_count, character_count)



main()



