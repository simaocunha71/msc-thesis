    total = 0
    for num in arr[:k]:
        total += sum(int(digit) for digit in str(num) if len(str(num)) <= 2)
    return total

