
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents

file_contents = "a waste of a day"

# Accept text from book as string

def count_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        split_words = file_contents.split()
    num_words = len(split_words)
    print(f"{num_words} words found in the document")



def main():
    #get_book_text('books/frankenstein.txt')
    count_words('books/frankenstein.txt')



main()

