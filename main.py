def count_words(text):
    return len(text.split())
    
def count_characters(text):
    char_dict = {}
    for char in text.lower():
        if char.isalpha():
            char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def generate_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    
    # Convert dictionary to list of dictionaries, filtering for alpha chars
    character_list = [
        {'char': char, 'count': count} 
        for char, count in count_characters(text).items()
    ]
    
    # Sort by count in descending order
    character_list.sort(key=lambda x: x['count'], reverse=True)
    
    for item in character_list:
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    generate_report(file_contents)

if __name__ == "__main__":
    main()