
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and str(num)[0] in '13579' and str(num)[-1] in '13579':
            count += 1
    return count

print(specialFilter([15, -73, 14, -15]))  # => 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # => 2

Here, we iterate over each number in the input array. For each number, we check if the number is greater than 10, and if the first and last digits of the number are odd (i.e., they are in the string '13579'). If both conditions are met, we increment our count. Finally, we return the count.
<jupyter_output>
<empty_output>
<jupyter_text>
**Question 2**: Write a Python function that takes a string as input and returns a dictionary where keys are unique words in the string and values are the counts of each word. For example, `wordCount("apple apple tree tree") => {'apple': 2, 'tree': 2}`.
<jupyter_code>
