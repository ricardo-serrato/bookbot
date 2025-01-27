
def main():
    path_to_frankenstein = "./books/frankenstein.txt"
    with open(path_to_frankenstein) as f:
        file_content = f.read()
        get_word_count = count_words(file_content)
        char_dict = get_character_count(file_content)
        list_of_dict_char = list_of_sub_dictionary(char_dict)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{get_word_count} words found in the document")
        for char_dict in list_of_dict_char:
            char = char_dict["char"]
            count = char_dict["count"]
            print(f"The '{char}' character was found {count} times")

def sort_on(dict):
    return dict["count"]
def list_of_sub_dictionary(dict):
    lst = []
    for key, value in dict.items():
        if key.isalpha():
            tmp_dict = {"char":key, "count":value}
            lst.append(tmp_dict)
    lst.sort(reverse=True, key=sort_on)
    return lst


def count_words(text):
    word_count = len(text.split())
    return word_count


def get_character_count(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


main()

