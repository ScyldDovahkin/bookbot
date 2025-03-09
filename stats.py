def text_to_words(content): #split the text into words
    words = content.split()
    return len(words)

def count_characters(content): #Count the words
    
    lower_cased = content.lower()
    characters = list(lower_cased)

    char_dict = {}
    
    for char in characters:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_dict(char_dict):
    # Create a list of dictionaries from the character dictionary
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    
    # Define a function to get the 'count' for sorting
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list by count in descending order
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
