    def sum_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    return sorted(nums, key=sum_digits)