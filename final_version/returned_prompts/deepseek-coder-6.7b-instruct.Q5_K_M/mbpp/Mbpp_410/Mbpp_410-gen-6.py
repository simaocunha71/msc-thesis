
def min_val(lst):
    numbers = [i for i in lst if isinstance(i, (int, float))]
    return min(numbers)

print(min_val(['Python', 3, 2, 4, 5, 'version']))

"""
In the function min_val, we use list comprehension to create a new list numbers which includes only the integers and floats from the given list. 
Then we use the built-in min function to find the minimum value in numbers and return this value.
"""
<jupyter_output>
2
<jupyter_text>
Question 2
<jupyter_code>
