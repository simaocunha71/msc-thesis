def count_nums(arr):
    def sum_digits(n):
        return sum(int(digit) for digit in str(abs(n)))

    return sum(1 for n in arr if sum_digits(n) > 0)

# Test cases
print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)