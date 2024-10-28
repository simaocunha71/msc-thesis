    return sorted(nums, key=lambda x: (sum(map(int, str(abs(x)))), -nums.index(x)))  # python 3.8 and above


