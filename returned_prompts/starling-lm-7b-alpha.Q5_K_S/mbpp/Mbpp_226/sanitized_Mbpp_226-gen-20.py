def odd_values_string(s):
    odd_index = ""
    for i in range(len(s)):
        if i % 2 != 0:
            odd_index += s[i]
    return odd_index