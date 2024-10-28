def is_polite(n):
    polite_numbers = set()
    i = 0
    while len(polite_numbers) < n:
        i += 1
        for j in range(1, i):
            if i - j in polite_numbers:
                polite_numbers.add(i)
                break
    return list(polite_numbers)[-1] if polite_numbers else None