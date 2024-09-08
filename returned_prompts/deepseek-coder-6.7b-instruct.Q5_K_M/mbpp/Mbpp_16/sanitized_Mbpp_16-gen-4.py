def text_lowercase_underscore(text):
    split_text = text.split('_')
    for word in split_text:
        if not word.islower():
            return False
    return True