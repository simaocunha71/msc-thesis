
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            str_num = str(abs(num))
            if str_num[0] in '13579' and str_num[-1] in '13579':
                count += 1
    return count

print(specialFilter([15, -73, 14, -15]))  # => 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # => 2
print(specialFilter([-1, 2, 3, 19, 21, 29]))  # => 3
print(specialFilter([-11, 2, 3, 19, 21, 29]))  # => 2
print(specialFilter([11, 2, 3, 19, 21, 29]))  # => 2
<jupyter_output>
1
2
3
2
2
<jupyter_text>
10. Write a function that takes an array of numbers and a number as inputs and returns the number of elements in the array that are greater than the input number.
<jupyter_code>
