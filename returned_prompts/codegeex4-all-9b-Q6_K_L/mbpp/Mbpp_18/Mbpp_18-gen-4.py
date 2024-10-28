def remove_dirty_chars(str1, str2):
    dirty_chars = set(str2)
    result = "".join([char for char in str1 if char not in dirty_chars])
    return result

