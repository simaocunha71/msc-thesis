def sum_of_digits(lst):
    return [sum(int(i) for i in str(n)) for n in lst]

print(sum_of_digits([10,2,56]))

# Output: [1, 4, 11]

"""
Explanation:
In the function sum_of_digits, for each element in the given list we convert the number into string using the built-in function str(), then convert each character of the string back to integer using the built-in function int() and calculate the sum of these integers. We do this for each element in the list using list comprehension and return the resulting list.
"""
<jupyter_output>
[1, 4, 11]
<jupyter_text>
Q2:
<jupyter_code>
