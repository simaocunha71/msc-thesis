    result = ''.join(char for char in s if char not in c)
    return result, result == result[::-1]  # check if the string is palindrome


