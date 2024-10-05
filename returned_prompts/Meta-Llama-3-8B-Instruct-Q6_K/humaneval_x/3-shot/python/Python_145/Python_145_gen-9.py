    return sorted(nums, key=lambda x: (sum(int(digit) for digit in str(abs(x))), -nums.index(x)))  # or sorted(nums, key=lambda x: (sum(int(digit) for digit in str(abs(x))), -id(x))) for Python 3.7+


