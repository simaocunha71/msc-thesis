    nums.sort(key=lambda x: sum(map(int, str(abs(x)))))
    return nums


