def unique_product(lst):
    unique_numbers = set(lst)
    product = 1
    for number in unique_numbers:
        product *= number
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))  # Output: 720000000


"""
The function works by first converting the list to a set, which automatically removes duplicates. Then it iterates over the unique numbers, multiplying them together.
"""
<jupyter_output>
720000000
<jupyter_text>
Problem 3:
<jupyter_code>
