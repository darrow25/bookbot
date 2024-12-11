def sort_on(dict):
    return dict["count"]
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)

        lowered_string = file_contents.lower()

        char_count = {}
        for char in lowered_string:
            if char in char_count:
                char_count[char] +=1
            else: char_count[char] = 1 

        char_list = []
        for char, count in char_count.items():
            if char.isalpha():
                char_list.append({"char": char, "count": count})

        char_list.sort(reverse=True, key=sort_on)

        print("--- begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        for char_dict in char_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
        print(" --- End repord ---")
    
                
        

main()