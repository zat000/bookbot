def count_words(text):
    split_text = text.split()
    return len(split_text)


def count_everything(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def char_list(dict1):
    new_list = []
    for char in dict1:
        new_dict = {}
        num = dict1[char]
        new_dict["char"] = char
        new_dict["num"] = num
        new_list.append(new_dict)
    return new_list
