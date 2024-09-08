
def unique_product(lst):
    # Using set to remove duplicates
    unique_lst = list(set(lst))
    product = 1
    for num in unique_lst:
        product *= num
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))  # Output: 720000000

"""
In the above solution, the set() function is used to remove duplicate elements from the list. Then, a for loop is used to calculate the product of the unique numbers.
"""

