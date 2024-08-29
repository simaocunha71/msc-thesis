def sum_of_digits(lst):
    res = []
    for num in lst:
        temp = 0
        for digit in str(num):
            temp += int(digit)
        res.append(temp)
    return res

print(sum_of_digits([10,2,56]))

# Output: [1, 2, 11]

# Explanation: 
# For the first number 10, the sum of its digits is 1 + 0 = 1
# For the second number 2, the sum of its digits is 2
# For the third number 56, the sum of its digits is 5 + 6 = 11
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
