
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_count_of_character(text)
    ascending_ordered_list = ascending_dictionary(chars_dict)
    print(f"-- Begin report of {book_path} --")
    print(f"{num_words} words found in the document \n")
    for d in ascending_ordered_list:
        for k in d:
            char = k
            count = d[char]

            print(f"The '{char}' character was found {count} times.")
    print('-- end report --')


def ascending_dictionary(dict):
    dictionary_list = []
    for k in dict:
        dictionary_list.append({k:dict[k]})

    dictionary_list.sort(key=sort_on,reverse=True)

    return dictionary_list




def sort_on(d):
    for key in d:
        return d[key]



def get_count_of_character(text):
    chars = {}
    for c in text:
        if not c.isalpha():
            continue
        c = c.lower()
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] +=1

    return chars


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

    
main()