    if not numbers:
        return []

    return numbers[:1] + [delimeter] + numbers[1:] + [delimeter] * (len(numbers) - 1)


