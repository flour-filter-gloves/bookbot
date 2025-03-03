def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    char_count = {}
    for char in file_contents:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1



    return char_count

def sort_chars_by_count():

    char_count = word_count()

    char_list = []
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char":char, "count":count})

    lst = sorted(char_list, key=lambda x: x["count"],reverse=True)
   
    
    return lst
def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    
    

    number_of_words = sort_chars_by_count()
    total_words = len((file_content).split()
)



    

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for dic in number_of_words:
        print(f"{dic["char"]}: {dic["count"]}")

    print("============= END ===============") 
main()