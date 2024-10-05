    result = 0
    for idx, letter in enumerate(s):
        if idx % 2 == 0:
            if letter.upper() in 'AEIOU':
                result += 1
    return result


