    result = ""
    for char in s:
        if char not in c:
            result += char

    return (result, result == result[::-1])  # check if the result is palindrome


