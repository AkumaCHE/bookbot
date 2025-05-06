from stats import get_word_count
from stats import char_count
from stats import char_dict_to_sorted_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # Count words and characters
    num_words = get_word_count(text)
    #print(f"{num_words} words found in the document")

    character_count_dict = char_count(text)
    #print(character_count_dict)


    # Call your new function to get a sorted list
    sorted_char_list = char_dict_to_sorted_list(character_count_dict)

    # Now you can print your report using word_count and sorted_chars_list
    def print_report(book_path, num_words, sorted_char_list):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        # Print each character and its count (we'll add filtering next)
        for char_dict in sorted_char_list:
            char = char_dict["char"]
            count = char_dict["num"]
                # Only print if it's an alphabetical character
            if char.isalpha():
                print(f"{char}: {count}")
        
        print("============= END ===============")

    print_report(book_path, num_words, sorted_char_list)




def get_book_text(path):
    with open(path) as f:
        return f.read()
    



    

main()