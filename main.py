def word_count(file_contents):
       
    char_count = {}
    for char in file_contents.lower():
            
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1



    return char_count

def is_a_alpha(file_contents):
    char_count = {}
    for word in file_contents:
        for char in word:
            char = char.lower()
            if char.isalpha():    
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

    lst = sorted(list(char_count.items()))

    return lst
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    number_of_words = file_contents.split()
    total_words = len(number_of_words)

    char_count = is_a_alpha(number_of_words)

    

    print("--- Begin report of books/frankenstein.txt ---")
    print(total_words)
    for pair in char_count:
        print(f"The '{pair[0]}' character was found {pair[1]} times")
    print("-- End report ---")
main()