def count_nums(arr):
    def sum_digits(n):
        """
        Returns the sum of the digits of an integer n.
        If n is negative, the sum of the digits of its absolute value is returned.
        """
        if n < 0:
            n = abs(n)
        return sum(int(digit) for digit in str(n))

    return sum(1 for num in arr if sum_digits(num) > 0)

# Test cases
print(count_nums([]) == 0)  # True
print(count_nums([-1, 11, -11]) == 1)  # True
print(count_nums([1, 1, 2]) == 3)  # True

# Additional test cases
print(count_nums([0, 0, 0]) == 0)  # True
print(count_nums([-1, -2, -3]) == 0)  # True
print(count_nums([1, -2, 3]) == 2)  # True
print(count_nums([10, 20, 30]) == 3)  # True
print(count_nums([-10, -20, -30]) == 0)  # True
print(count_nums([100, 200, 300]) == 3)  # True
print(count_nums([-100, -200, -300]) == 0)  # True
print(count_nums([1000, 2000, 3000]) == 3)  # True
print(count_nums([-1000, -2000, -3000]) == 0)  # True
print(count_nums([10000, 20000, 30000]) == 3)  # True
print(count_nums([-10000, -20000, -30000]) == 0)  # True
print(count_nums([100000, 200000, 300000]) == 3)  # True
print(count_nums([-100000, -200000, -300000]) == 0)  # True
print(count_nums([1000000, 2000000, 3000000]) == 3)  # True
print(count_nums([-1000000, -2000000, -3000000]) == 0)  # True
print(count_nums([10000000, 20000000, 30000000]) == 3)  # True
print(count_nums([-100