    def sum_of_digits(n):
        return sum(map(int, str(n).replace('-', '')))

    return sorted(nums, key=lambda n: (sum_of_digits(n), nums.index(n)))

