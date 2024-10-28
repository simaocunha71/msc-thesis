    def is_even(num):
        return num % 2 == 0

    def get_even_digits(num):
        return [int(digit) for digit in str(num) if is_even(int(digit))]

    result = []
    for num in range(a, b + 1):
        if is_even(num):
            result.extend(get_even_digits(num))

    return result

