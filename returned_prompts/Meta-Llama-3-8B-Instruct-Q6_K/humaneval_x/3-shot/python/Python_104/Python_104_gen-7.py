    return sorted([num for num in x if not any(int(digit) % 2 == 0 for digit in str(num))])  # noqa: E501


