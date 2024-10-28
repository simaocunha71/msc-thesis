def is_nonagonal(n):
    if n < 1:
        return None
    nonagonal_numbers = [1]
    while len(nonagonal_numbers) < n:
        nonagonal_numbers.append(nonagonal_numbers[-1] + 9*len(nonagonal_numbers))
    return nonagonal_numbers[-1]