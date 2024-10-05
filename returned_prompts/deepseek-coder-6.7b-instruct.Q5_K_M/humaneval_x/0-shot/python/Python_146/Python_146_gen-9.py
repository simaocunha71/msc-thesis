
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and str(abs(num))[0] in '13579' and str(abs(num))[-1] in '13579':
            count += 1
    return count

print(specialFilter([15, -73, 14, -15]))  # 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # 2

'''
The function specialFilter iterates over each number in the input list. 
For each number, it checks if the number is greater than 10 and if the first and last digits of the absolute value of the number are in '13579'. 
If both conditions are met, it increments the count variable. Finally, it returns the count.
'''
<jupyter_output>
1
2
<jupyter_text>
Problem 2: Find the Shortest Path in a Grid
<jupyter_code>
