def capital_words_spaces(text):
    result = ''
    for letter in text:
        if letter.isupper():
            result += ' '
        result += letter
    return result.strip()