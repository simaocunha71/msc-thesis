    def sum_of_digits(n):
        return sum(int(i) for i in str(n) if i.isdigit())

    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))


