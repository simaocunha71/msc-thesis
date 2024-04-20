"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""

def find_largest_products(a, b):
    """Function to find the specified number of largest products from two given lists, selecting one factor from each list."""

    # Sorting our input
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    
    return [i*j for i in a for j in b]
