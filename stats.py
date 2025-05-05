# Accept text from book as string and prints word count
def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        split_words = file_contents.split()
    num_words = len(split_words)
    print(f"{num_words} words found in the document")