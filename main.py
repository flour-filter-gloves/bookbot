from stats import sort_chars_by_count
import sys
def main():
    if len(sys.argv)  < 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_content = f.read()
    
    

    number_of_words = sort_chars_by_count(sys.argv[1])
    total_words = len((file_content).split()
)



    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}..")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for dic in number_of_words:
        print(f"{dic["char"]}: {dic["count"]}")

    print("============= END ===============") 
main()