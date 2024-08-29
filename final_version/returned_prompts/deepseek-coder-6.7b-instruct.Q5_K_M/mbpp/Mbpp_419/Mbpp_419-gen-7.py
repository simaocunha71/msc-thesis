def round_and_sum(lst):
    rounded = [round(num) for num in lst]
    return sum(rounded) * len(lst)

print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))  # 243

# Output: 243

"""
Explanation:
The function `round_and_sum()` takes a list of numbers as input. It uses a list comprehension to create a new list where each number is rounded to the nearest integer. It then returns the sum of this new list multiplied by the length of the original list.
"""
<jupyter_output>
243
<jupyter_text>
Question 2:
<jupyter_code>
