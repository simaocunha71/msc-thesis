    result = ''
    is_letter = False
    for i in s:
        if i.isalpha():
            is_letter = True
            if i.islower():
                result += i.upper()
            else:
                result += i.lower()
        else:
            result += i
    if not is_letter:
        result = result[::-1]
    return result
