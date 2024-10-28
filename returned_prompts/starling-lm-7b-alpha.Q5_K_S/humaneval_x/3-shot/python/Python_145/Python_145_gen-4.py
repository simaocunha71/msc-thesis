    def sum_digits(num):
        return sum(map(int, str(num)))

    def key_func(num):
        return -sum_digits(num), num

    return sorted(nums, key=key_func)


