def extract_values(string):
    start = string.find('"')
    end = string.rfind('"')
    return string[start + 1 : end]