def text_lowercase_underscore(text):
    for i in range(len(text)-1):
        if not text[i].islower() or not text[i+1].islower():
            if text[i] != '_':
                return False
    return True