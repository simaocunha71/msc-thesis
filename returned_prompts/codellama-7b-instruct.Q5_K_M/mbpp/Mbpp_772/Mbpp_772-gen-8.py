
def remove_length(input_str, k):
    return ' '.join([word for word in input_str.split() if len(word) != k])


