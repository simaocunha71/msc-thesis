    result = ''.join([c for c in s if c not in c])
    return result, result == result[::-1]  # check if the result string is palindrome


