    return sorted(range(len(nums)), key=lambda i: sum(map(int, str(abs(nums[i])))) * (1 if nums[i] >= 0 else -1))


