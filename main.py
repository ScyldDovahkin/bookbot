import sys
from stats import text_to_words #Function in stats.py
from stats import count_characters #Function in stats.py
from stats import sort_dict #Returns sorted dictionary

def get_book_text(path_to_file): #path to file is  a string
    file_contents = ""

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents #File contents is all the words in the text, stored with 'open as' function


def main():
    if len(sys.argv) > 1:
            
        book_text = get_book_text(sys.argv[1])
        word_count= text_to_words(book_text)
        character_dict = count_characters(book_text)

        sorted_chars = sort_dict(character_dict)

        # Print the report header
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
    
        #  Print the word count section
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
    
        # Print the character count section
        print("--------- Character Count -------")
    
        # Loop through the sorted characters and print only alphabetical ones
        for char_dict in sorted_chars:
            char = char_dict["char"]
            count = char_dict["count"]
        
            # Only print alphabetical characters
            if char.isalpha():
                print(f"{char}: {count}")
    
    # Print the report footer
        print("============= END ===============")
    
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
main()
