def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = count_words(text)
    charcount = no_of_times(text)
    chars_sorted_list = chars_dict_to_sorted_list(charcount)
    #print(f"Word count: {wordcount}, char_count: {charcount}")
    print("""--- Begin report of books/frankenstein.txt ---""")
    print(f"{wordcount} words found in the document\n")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def no_of_times(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    
def count_words(text):
    words = text.split()
    return len(words)


main()