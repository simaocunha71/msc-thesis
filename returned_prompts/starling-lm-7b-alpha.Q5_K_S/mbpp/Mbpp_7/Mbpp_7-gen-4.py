"""

def find_char_long(input_str):
    # Split the string into words
    words = input_str.split()
    # Initialize an empty set to store the result
    result = set()
    # Iterate through the list of words and add to result if the length is at least 4
    for word in words:
        if len(word) >= 4:
            result.add(word)
    return result


"""
