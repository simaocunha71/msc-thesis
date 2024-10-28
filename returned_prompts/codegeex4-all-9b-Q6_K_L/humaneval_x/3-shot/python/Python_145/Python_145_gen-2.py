    def sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    return sorted(nums, key=sum_of_digits)

