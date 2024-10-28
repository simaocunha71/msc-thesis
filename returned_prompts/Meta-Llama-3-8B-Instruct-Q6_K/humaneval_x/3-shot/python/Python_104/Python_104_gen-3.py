    return sorted([num for num in x if not any(int(digit) % 2 == 0 for digit in str(num))])  # Python3.8+
    # return sorted([num for num in x if not any(int(digit) % 2 == 0 for digit in str(num))][::-1])  # Python3.7-


