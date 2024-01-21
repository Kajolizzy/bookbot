from operator import itemgetter

def main():
    book_path = "books/frankenstein.txt"
    whole_text = get_book_text(book_path)
    word_counter = get_num_word(whole_text)
    letter_counter = get_num_letters(whole_text)
    sorted_letter_counter_list = get_sorted_letter_counter_list(letter_counter)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_counter} words found in the document")
    print("")
    for tuple in sorted_letter_counter_list:
        print(f"The '{tuple[0]}' character was found {tuple[1]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_num_word(text):
    word_counter = 0
    words = text.split()
    for word in words:
        word_counter += 1
    return word_counter

def get_num_letters(text):
    letter_counter = {}
    for letter in text:
        letter = letter.lower()
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1
    return letter_counter

def get_sorted_letter_counter_list(dict):
    sorted_list = []
    for entry in dict:
        if entry.isalpha() == True:
            sorted_list.append((entry, dict[entry]))
        sorted_list = sorted(sorted_list, key = itemgetter(1), reverse = True)
    return sorted_list

if __name__ == "__main__":
    main()