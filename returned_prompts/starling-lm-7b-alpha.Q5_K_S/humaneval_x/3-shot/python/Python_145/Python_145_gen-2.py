    def sum_of_digits(num):
        return sum(map(int, str(num)))

    def idx(num):
        return nums.index(num)

    return sorted(nums, key=lambda x: (sum_of_digits(x), idx(x)))


