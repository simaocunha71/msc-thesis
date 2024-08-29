def find_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

print(find_evens([1,2,3,4,5]))

# Output: [2, 4]

# This function uses list comprehension to iterate over the input list and return a new list of the numbers that are even (i.e., when divided by 2, leave a remainder of 0).
<jupyter_output>
[2, 4]
<jupyter_text>
Q2:Write a Python function to find the elements in a list that are divisible by an integer.
<jupyter_code>
