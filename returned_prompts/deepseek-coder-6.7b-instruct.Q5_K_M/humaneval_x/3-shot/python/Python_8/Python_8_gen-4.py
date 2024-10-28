    if not numbers:
        return 0, 1
    else:
        product = 1
        for num in numbers:
            product *= num
        return sum(numbers), product


