    def sum_of_digits(n):
        return sum(int(digit) for digit in str(abs(n)))

    return sorted(nums, key=sum_of_digits)

