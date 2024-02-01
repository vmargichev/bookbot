def main():
    with open("books/frankenstein.txt") as f:
        reading = f.read()
        print(reading)
    print(get_count_words(reading))

def get_count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count


main()
