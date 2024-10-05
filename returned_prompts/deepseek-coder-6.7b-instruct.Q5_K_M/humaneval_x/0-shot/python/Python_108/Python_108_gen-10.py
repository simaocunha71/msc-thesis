
    def sum_digits(n):
        s = 0
        while n:
            digit = n % 10
            s += digit
            n //= 10
        return s

    return sum(sum_digits(i) > 0 for i in arr)

print(count_nums([]))  # 0
print(count_nums([-1, 11, -11]))  # 1
print(count_nums([1, 1, 2]))  # 3

# The function sum_digits calculates the sum of the digits of a number.
# Then, for each number in the array, it adds 1 to a counter if the sum of its digits is greater than 0.
# The function count_nums returns the final count.

# The time complexity of the solution is O(n*m), where n is the length of the array and m is the average number of digits in the numbers.
# The space complexity is O(1), as no additional space is used.
<jupyter_output>
0
1
3
<jupyter_text>
Problem 2:
<jupyter_code>
