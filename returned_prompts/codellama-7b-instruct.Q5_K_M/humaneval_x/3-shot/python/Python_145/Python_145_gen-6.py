    return sorted(nums, key=lambda num: sum(map(int, str(abs(num)))))


