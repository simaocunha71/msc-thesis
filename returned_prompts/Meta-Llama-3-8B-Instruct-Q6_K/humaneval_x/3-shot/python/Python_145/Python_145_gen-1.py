    return sorted(nums, key=lambda x: (sum(map(int, str(abs(x)))), nums.index(x)))  # or sorted(nums, key=lambda x: (sum(map(int, str(abs(x)))), x)) in Python 3.7+


