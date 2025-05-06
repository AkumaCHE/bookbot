def get_word_count(text):
    word_count = text.split()
    return len(word_count)



def char_count(text):

    lower_case_text = text.lower()
    my_dict = {}
    
    for char in lower_case_text:
        if char in my_dict:
            my_dict[char] +=  1
        else:
            my_dict[char] = 1
                
    return my_dict


def char_dict_to_sorted_list(character_count_dict):
    char_list = []
    for char, count in character_count_dict.items():
        # Create a new dictionary for this character
        char_info = {"char": char, "num": count}
        # Add this dictionary to our list
        char_list.append(char_info)
    # Define a function to tell sort() which value to use
    def sort_on(dict):
        return dict["num"]
    # Sort the list in descending order (reverse=True)
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
    









    