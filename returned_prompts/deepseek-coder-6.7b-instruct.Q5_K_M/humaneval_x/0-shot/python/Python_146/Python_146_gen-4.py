
def specialFilter(nums):
    count = 0
    for num in nums:
        if abs(num) > 10 and str(abs(num))[0] in '13579' and str(abs(num))[-1] in '13579':
            count += 1
    return count

print(specialFilter([15, -73, 14, -15]))  # 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # 2

# Note: The function abs() is used to handle negative numbers, as the requirement 
#       states that we only care about the last digit.

#       The function str() is used to convert the number into a string to easily 
#       access its digits.
<jupyter_output>
1
2
<jupyter_text>
Question 5:
<jupyter_code>
