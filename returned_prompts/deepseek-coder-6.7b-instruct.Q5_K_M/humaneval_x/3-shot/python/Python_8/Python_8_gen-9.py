    if not numbers:
        return 0, 1

    sum_ = 0
    product = 1

    for num in numbers:
        sum_ += num
        product *= num

    return sum_, product


