def find_char_long(sentence):
    char_list = sentence.split()
    char_list = [i for i in char_list if len(i) >= 4]
    return char_list
sentence = 'Please move back to stream'