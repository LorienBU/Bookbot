def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_num_chars(text)
    print('------Begin report of Frankenstein book------')
    print(f'The book has {num_words} words.')
    
    for item in chars:
        print(f"The '{item["char"]}' character was found {item["num"]} times.")    
    
    print("-------The end of the report.-------")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def get_num_words(x):
    words = x.split()
    return len(words)

def sort_on(d):
    return d["num"]

def get_num_chars(text):
    text_lower = text.lower()
    chars_dict = {}
    for char in text_lower:        
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1   
    
    chars_list = [{"char": dict, "num": chars_dict[dict] } for dict in chars_dict if dict.isalpha()]
    chars_list.sort(reverse=True, key=sort_on)    
    return chars_list


main()
