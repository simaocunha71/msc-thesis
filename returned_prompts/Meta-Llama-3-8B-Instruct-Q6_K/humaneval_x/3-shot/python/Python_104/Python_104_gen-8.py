    return sorted([i for i in x if not any(int(digit) % 2 == 0 for digit in str(i))])  # or using list comprehension


