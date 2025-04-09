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