def is_polite(n):
    polite_numbers = []
    i = 1
    while len(polite_numbers) < n:
        if i % 2 == 0:
            polite_numbers.append(i - 1)
        else:
            polite_numbers.append(i)
        i += 1
    return polite_numbers[-1]  # return the nth polite number