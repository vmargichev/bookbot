def main():
    print(get_text())
    print(get_count_words(get_text()))

def get_count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count
def get_text():
    with open("books/frankenstein.txt") as f:
        return f.read()
    

main()
