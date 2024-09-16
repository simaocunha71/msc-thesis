def remove_dirty_chars(str1, str2):
    return ''.join([i for i in str1 if i not in str2])