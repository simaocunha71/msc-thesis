def extract_quotation(string):
    tokens = string.split(' ')
    result = []
    for token in tokens:
        if token[0] == '"' and token[-1] == '"':
            result.append(token[1:-1])
    return result