import string
lower_case_alphabet = list(string.ascii_lowercase)

def main():
    print(get_count_words(get_text()))

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
    occur_dict = {}
    lower = lower_text(text)
    words = lower.split()
    for char in lower_case_alphabet:
        for word in words:   
            if char in word and occur_dict[char] == 0:
                occur_dict[char] == 1
            elif char in word and occur_dict[char] > 0:
                occur_dict[char] += 1
    return occur_dict

    

main()
