def Split(list):
    return [num for num in list if num % 2 != 0]

print(Split([1,2,3,4,5,6]))

# Output: [1, 3, 5]

# Explanation: The function uses list comprehension to iterate over each number in the input list. If the number is not divisible by 2 (i.e. it is odd), it is included in the output list.
<jupyter_output>
[1, 3, 5]
<jupyter_text>
Question 2: Write a Python function that takes a list and returns a new list with unique elements of the first list.
<jupyter_code>
