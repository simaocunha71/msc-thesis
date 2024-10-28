    def digit_sum(n):
        return sum(int(digit) for digit in str(abs(n)))

    return sorted(nums, key=digit_sum)

