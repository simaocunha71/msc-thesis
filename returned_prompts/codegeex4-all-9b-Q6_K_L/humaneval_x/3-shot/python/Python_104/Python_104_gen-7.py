    result = []

    for num in x:
        even_digit = False
        for digit in str(num):
            if int(digit) % 2 == 0:
                even_digit = True
                break
        if not even_digit:
            result.append(num)

    return sorted(result)