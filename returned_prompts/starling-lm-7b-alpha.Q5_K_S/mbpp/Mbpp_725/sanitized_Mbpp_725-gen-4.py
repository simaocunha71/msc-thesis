def extract_quotation(s):
    values = []
    for word in s.split():
        if word.startswith('"') and word.endswith('"'):
            values.append(word[1:-1])
    return values