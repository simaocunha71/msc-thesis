    def sum_of_digits(n):
        if n < 0:
            n = -n
        return sum(int(digit) for digit in str(n))

    return sorted(nums, key=lambda n: (sum_of_digits(n), nums.index(n)))

