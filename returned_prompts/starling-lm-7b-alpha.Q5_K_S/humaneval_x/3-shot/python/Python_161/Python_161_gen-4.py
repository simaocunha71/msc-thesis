    result = ""
    for elem in s:
        if elem.isalpha():
            result += chr(ord(elem) ^ 32)
        else:
            result += elem
    return result[::-1]


