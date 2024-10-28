def text_lowercase_underscore(text):
    text_split = text.split('_')
    for word in text_split:
        if not word.islower():
            return False
    return True

