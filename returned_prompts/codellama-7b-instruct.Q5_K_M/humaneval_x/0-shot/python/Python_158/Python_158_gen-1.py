
def find_max(words):
    if not words:
        return ""
    max_len = 0
    result = ""
    for i in words:
        if len(set(i)) > max_len:
            max_len = len(set(i))
            result = i
    return result
