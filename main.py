def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    #print(file_content)
    letter_count = {}
    letter_count = counts(file_content)
    print(letter_count)
    sort_by_items = sorting(letter_count)

def letter_count(file_content):
    words = file_content.split()
    print(len(words) ,"words are found in the document")
    return len(words)
    
def counts(file_content):
    file_content=file_content.lower()
    letter_count = {char: file_content.count(char) for char in "abcdefghijklmnopqrstuvwxyz"}
    return letter_count

def sorting(letter_count):
    sorted_by_keys = {}
    sorted_by_keys = dict(sorted(letter_count.items() ,key=lambda x: x[1],  reverse = True))
    for key, values in sorted_by_keys.items():
        print(f"The '{key}' charactor was found {values}")

if __name__ == "__main__":
    main()
