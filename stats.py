def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_num_characters(text):
    text = text.lower()
    num_dict = {}
    for t in text:
        if t in num_dict:
            num_dict[t] += 1
        else:
            num_dict[t] = 1
    
    return num_dict

def sort_characters(char_dict):
    sorted_characters = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_characters