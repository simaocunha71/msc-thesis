def remove_lowercase(s):
    result = ''
    current_substring = ''
    for char in s:
        if char.isupper():
            current_substring += char
        else:
            if current_substring not in result:
                result += current_substring
            current_substring = ''
    if current_substring not in result:
        result += current_substring
    return result