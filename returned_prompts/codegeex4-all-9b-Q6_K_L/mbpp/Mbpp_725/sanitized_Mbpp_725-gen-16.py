def extract_quotation(string):
    string_list = string.split()
    result = []
    for word in string_list:
        if word.startswith('"') and word.endswith('"'):
            result.append(word[1:-1])
    return result