def unique_product(lst):
    product = 1
    for i in set(lst):
        product *= i
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))

# Another solution

def unique_product(lst):
    unique_numbers = set(lst)
    product = 1
    for num in unique_numbers:
        product *= num
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))


"""
The function 'unique_product' takes in a list 'lst' and returns the product of the unique numbers in the list. 
It does this by first converting the list into a set, which automatically removes any duplicate elements. 
Then it multiplies together all the elements in the set, which gives the product of the unique numbers in the list.
"""
<jupyter_output>
720000000
720000000
<jupyter_text>
2. Write a Python function to find the maximum and minimum numbers from a given list of numbers.
<jupyter_code>
