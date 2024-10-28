    result = 0

    for num in arr:
        is_positive = True
        signed_digits = []

        if num < 0:
            is_positive = False
            num = -num

        while num > 0:
            signed_digits.append(num % 10)
            num //= 10

        if is_positive:
            signed_digits.reverse()

        if any(sum(signed_digits[i:] > 0 for i in range(len(signed_digits))):
            result += 1

    return result


