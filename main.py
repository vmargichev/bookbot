import string
def main():
    print_report(get_occur_times(get_text()))
    
def print_report(dict):
    result_list = list(dict)
    result_list.sort()
    print(result_list)
    # for i in result_list:
        # if i.isalpha():
            # print(f"The {i} character was found {dict[i]} times")

def split_text(text):
    splited_text = text.split()
    return splited_text

def get_count_words(text):
    words = split_text(text)
    count = 0
    for word in words:
        count += 1
    return count

def get_text():
    with open("books/frankenstein.txt") as f:
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
