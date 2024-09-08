def Split(lst):
    return [num for num in lst if num % 2 != 0]

print(Split([1,2,3,4,5,6]))

# Split function uses list comprehension to create a new list that only contains the odd numbers. It does this by iterating through each number in the original list and checking if the modulus of the number is not equal to 0 (which would mean the number is odd). If this is the case, the number is added to the new list.
<jupyter_output>
[1, 3, 5]
<jupyter_text>
2. Write a Python function to multiply all the numbers in a list.
<jupyter_code>
