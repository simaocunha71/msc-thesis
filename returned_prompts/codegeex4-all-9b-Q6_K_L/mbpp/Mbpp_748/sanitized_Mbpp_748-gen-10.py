def capital_words_spaces(s: str) -> str:
    result = ''
    for char in s:
        if char.isupper():
            result += ' ' + char
        else:
            result += char
    return result.strip()