    result = s
    for c in set(c):
        result = result.replace(c, '')
    return result, result == result[::-1]  # check if result is palindrome


