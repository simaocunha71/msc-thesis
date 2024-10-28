    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    return sorted(nums, key=lambda num: (sum_of_digits(num), nums.index(num)))

