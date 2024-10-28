    nums.sort(key=lambda num: (sum(map(int, str(abs(num)))), num))
    return nums


