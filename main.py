
def main():
    print("Welcome to bookbot")
    path_to_book = './books/frankenstein.txt'

    try:
        book_text = get_book_text(path_to_book)
        word_count = get_word_count(book_text)
        letter_dict = get_letter_count(book_text)
        letter_list = convert_to_list(letter_dict)
        letter_list.sort(reverse=True, key=sort_on)

        # Sorts the list by occurence
        for item in letter_list:
            print(sort_on(item))
        
        print(f"--- Begin report of {path_to_book}")
        print(f"{word_count} words found in the document\n")
        for item in letter_list:
            print(f"{item['key']} character was found {item['count']} times")

        print('--- End Report ---')
    
    except OSError:
        print("Read is hard")

def get_word_count(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_letter_count(text):
    letters = {}
    for letter in text:
        lower_case_letter = letter.lower()
        if not lower_case_letter.isalpha():
            continue
        
        if (lower_case_letter in letters):
            letters[lower_case_letter] += 1
        else:
            letters[lower_case_letter] = 1
            
    return letters

def convert_to_list(dictionary):
    def standardize(items):
        return { "key": items[0], "count": items[1] }
    
    return list(map(standardize, dictionary.items()))

def sort_on(dict):
    return dict["count"]

main()
