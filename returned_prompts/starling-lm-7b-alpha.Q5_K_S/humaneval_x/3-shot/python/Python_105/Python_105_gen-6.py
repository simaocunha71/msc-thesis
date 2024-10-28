    numbers = [str(n) for n in arr if 1 <= n <= 9]
    numbers.sort(reverse=True)
    result = [name for n in numbers for name in by_length]
    return result


