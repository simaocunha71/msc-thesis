def count_nums(arr):
    def sum_digits(n):
        """Return the sum of the digits of n."""
        return sum(int(digit) for digit in str(n))

    return sum(1 for num in arr if sum_digits(num) > 0)

print(count_nums([]) == 0)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([1, 1, 2]) == 3)
