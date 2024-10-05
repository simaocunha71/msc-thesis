    result = ''
    for i in s:
        if i.isalpha():
            if i.islower():
                result += i.upper()
            else:
                result += i.lower()
        else:
            result += i

    if result.isalpha():
        return result
    else