    return sorted([digit for digit in x if not any(digit % 2 == 0 for digit in str(digit))])


