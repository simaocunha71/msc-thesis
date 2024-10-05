    def sum_of_digits(n):
        return sum(map(int, str(abs(n))))

    return sorted(nums, key=sum_of_digits)

