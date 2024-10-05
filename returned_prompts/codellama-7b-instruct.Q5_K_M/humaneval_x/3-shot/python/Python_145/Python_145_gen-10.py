    def get_sum(x):
        sum = 0
        for c in str(x):
            sum += int(c)
        return sum

    nums.sort(key=lambda x: (get_sum(x), x))
    return nums


