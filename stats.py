def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def char_count(file_contents):
    running_totals = {}
    for char in file_contents:
        char = char.lower()
        if char in running_totals:
            running_totals[char] += 1
        else:
            running_totals[char] = 1
    return running_totals

def sort_on(char_count_dict_element):
    return char_count_dict_element['num']

def sort_char_count(char_count_dict):
    char_count_list = []
    for char, count in char_count_dict.items():
        if char.isalpha():
            char_count_list.append({'char': char, 'num': count})
        else:
            pass
    char_count_list.sort(key=sort_on, reverse=True)
    return char_count_list




