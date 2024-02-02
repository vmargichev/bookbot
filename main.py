import string
file_path = "books/frankenstein.txt"

def main():
    text = get_text(file_path)
    char_dict = get_occur_times(text)
    char_list_sorted = chars_dict_to_sorted_list(char_dict)
    print(f"--- Begin report of {file_path} ---")
    print(f"{get_count_words(text)} words found in the document")
    print()
    for item in char_list_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char" : c, "num": dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]    

def split_text(text):
    splited_text = text.split()
    return splited_text

def get_count_words(text):
    words = split_text(text)
    count = 0
    for word in words:
        count += 1
    return count

def get_text(path):
    with open(path) as f:
        return f.read()

def lower_text(text):
    lower_text = text.lower()
    return lower_text

def get_occur_times(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()
