from stats import get_num_words

# Accept text from book as string and prints text
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
    print(file_contents)


def main():
    #get_book_text('books/frankenstein.txt')
    get_num_words('books/frankenstein.txt')



main()

