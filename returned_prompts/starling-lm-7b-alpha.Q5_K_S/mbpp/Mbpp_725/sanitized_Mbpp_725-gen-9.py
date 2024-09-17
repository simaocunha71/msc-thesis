import re
def extract_quotation(s):
    result = []
    index = 0
    while index < len(s):
        if s[index] == '"':
            start = index + 1
            index += 1
            while s[index] != '"':
                result.append(s[start:index])
                index += 1
            index += 1
        else:
            index += 1
    return result