def is_polite(n):
    polite_numbers = []
    num = 1
    while len(polite_numbers) < n:
        if all(num - i > 0 for i in range(1, num)):
            polite_numbers.append(num)
        num += 1
    return polite_numbers[-1] if polite_numbers else None