def books_number_words(text):
    words = text.split()
    return len(words)
    
def num_of_characters(text):
    char_count = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(dict):
    return dict["count"]

def print_report(dict_chars):
    sorted_list = []
    for key, value in dict_chars.items():
        char_dict = {"char": key, "count": value}
        sorted_list.append(char_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list