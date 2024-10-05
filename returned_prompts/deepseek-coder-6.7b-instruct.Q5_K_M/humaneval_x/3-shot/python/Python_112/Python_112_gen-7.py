    result = [x for x in s if x not in c]
    rev_result = result[::-1]
    is_palindrome = result == rev_result
    return ("".join(result), is_palindrome)


