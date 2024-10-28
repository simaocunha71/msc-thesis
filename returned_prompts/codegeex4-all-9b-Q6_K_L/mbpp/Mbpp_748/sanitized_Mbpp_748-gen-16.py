def capital_words_spaces(text):
    text = text[0].upper() + text[1:]
    return " ".join([word for word in text.split() if word[0].isupper()])