    result = [i for i in s if i not in c]
    return (''.join(result), ''.join(result) == ''.join(result)[::-1])  # Check if the string is palindrome


