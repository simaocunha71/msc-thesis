def sum_of_digits(lst):
    res = []
    for num in lst:
        sum_digits = 0
        for digit in str(num):
            sum_digits += int(digit)
        res.append(sum_digits)
    return res

print(sum_of_digits([10,2,56]))

# Output: [1, 2, 11]

# Explaination:
# For the number 10, the sum of its digits is 1 + 0 = 1.
# For the number 2, the sum of its digits is 2.
# For the number 56, the sum of its digits is 5 + 6 = 11.

# So, the function returns [1, 2, 11].

# Complexity Analysis:
# The time complexity of this approach is O(n*m), where n is the number of elements in the list and m is the number of digits in the largest number.
# The space complexity is O(n), as we are storing the sum of digits for each number in the list.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2
<jupyter_code>
