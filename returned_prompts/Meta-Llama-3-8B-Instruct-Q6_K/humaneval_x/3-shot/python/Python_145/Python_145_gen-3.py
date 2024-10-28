    return sorted(nums, key=lambda x: (sum(int(digit) for digit in str(abs(x))), nums.index(x)))  # your code here


