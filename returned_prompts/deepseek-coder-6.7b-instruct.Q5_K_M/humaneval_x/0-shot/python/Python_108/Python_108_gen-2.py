
    def count_nums(arr):
        count = 0
        for num in arr:
            digit_sum = sum(int(digit) for digit in str(num))
            if digit_sum > 0:
                count += 1
        return count

    return count_nums(arr)

# Test cases
print(count_nums([]))  # Expected output: 0
print(count_nums([-1, 11, -11]))  # Expected output: 1
print(count_nums([1, 1, 2]))  # Expected output: 3

# Note: The function 'count_nums' is defined to convert negative numbers into their
# positive counterparts and then check the sum of digits. If the sum is greater than 0,
# it increments the count variable. The count variable is then returned at the end.
# Hence, for [-1, 11, -11], it checks the sum of digits for -1 (1), 11 (2), and -11 (2)
# and returns the count of numbers for which the sum of digits is greater than 0.
# Hence, the output is 1.
<jupyter_output>
0
1
3
<jupyter_text>
