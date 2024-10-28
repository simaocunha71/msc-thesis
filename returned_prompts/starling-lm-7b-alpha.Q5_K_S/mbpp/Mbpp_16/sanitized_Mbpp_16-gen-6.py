def text_lowercase_underscore(s):
    # Split the string into words
    words = s.split('_')
    # Check if all words are lowercase
    return all(word.lower() == word for word in words)