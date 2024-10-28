    return sorted(nums, key=lambda x: (sum(int(i) for i in str(abs(x))), nums.index(x)))


