def word_count(args):
    with open(args) as f:
        file_contents = f.read()
    char_count = {}
    for char in file_contents:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1



    return char_count

def sort_chars_by_count(args):

    char_count = word_count(args)

    char_list = []
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char":char, "count":count})

    lst = sorted(char_list, key=lambda x: x["count"],reverse=True)
   
    
    return lst