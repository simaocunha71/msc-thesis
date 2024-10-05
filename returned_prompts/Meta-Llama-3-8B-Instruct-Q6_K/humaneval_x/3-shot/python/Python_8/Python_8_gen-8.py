    if not numbers:
        return 0, 1
    else:
        return sum(numbers), 1 if len(numbers) == 0 else 1 * prod(numbers)


