    def sum_digits(n):
        if n < 0:
            n = -n
        return sum(int(i) for i in str(n))

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))


