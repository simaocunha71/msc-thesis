def reverse_words(sentence):
    """
    Reverse words separated by spaces in a given string
    """
    words = sentence.split(' ')
    return ' '.join(words[::-1])