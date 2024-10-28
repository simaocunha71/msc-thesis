def extract_quotation(s):
    result = []
    quote = False
    current_word = ''
    for char in s:
        if char == '"':
            if quote:
                result.append(current_word)
                current_word = ''
            quote = not quote
        elif quote:
            current_word += char
    return result