def remove_length(string, k):
    new_string = ""
    for word in string.split():
        if len(word) != k:
            new_string += word + " "
    return new_string[:-1]