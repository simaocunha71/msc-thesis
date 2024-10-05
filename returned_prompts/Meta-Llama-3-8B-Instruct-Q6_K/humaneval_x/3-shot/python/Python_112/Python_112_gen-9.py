    result = [char for char in s if char not in c]
    return (''.join(result), ''.join(result) == ''.join(result)[::-1])  # check if the result string is palindrome


