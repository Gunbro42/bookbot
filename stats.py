# Home of multiple different stat functions
def sort_on(dict):
    return dict["num"]
# Sorting helper key

def word_count(text):
    total_words = text.split()
    return len(total_words)
# Returns word count total

def get_char_counts(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    list_sort = []
    keys = char_dict.keys()
    for key in keys:
        list_sort.append({"name": key, "num": char_dict[key]})
    list_sort.sort(reverse=True, key=sort_on)
    char_dict = {}
    for dictionary in list_sort:
        char_dict[dictionary['name']] = dictionary['num']
    return char_dict
