# Accept text from book as string and prints word count
def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        split_words = file_contents.split()
    num_words = len(split_words)
    print(f"{num_words} words found in the document")


def count_char(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        lower_case_file_contents = file_contents.lower()
        # Use a dictionary of String -> Integer. {'p': 6121,...}
        #First, we will create an empty python dictionary using the dict() function.
        my_dict = {}
        #Next, we will use a for loop to iterate through the characters of the string.
        for char in lower_case_file_contents:
        # While iteration, we will first check if the character is already present in the dictionary or not. 
            if char in my_dict:
        # #If yes, we will increment the value associated with the character in the dictionary.
                my_dict[char] +=  1
        # #Otherwise, we will assign the character as a key and 1 as the associated value to the dictionary.
            else:
                my_dict[char] = 1
                
    print(my_dict)