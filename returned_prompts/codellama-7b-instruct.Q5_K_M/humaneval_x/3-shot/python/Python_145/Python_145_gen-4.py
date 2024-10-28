    def key_function(x):
        digits = [int(i) for i in str(x)]
        sum_of_digits = sum(digits)
        return sum_of_digits, x

    return sorted(nums, key=key_function)


