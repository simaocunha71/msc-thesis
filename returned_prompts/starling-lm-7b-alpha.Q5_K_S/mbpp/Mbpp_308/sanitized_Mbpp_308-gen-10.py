def large_product(nums_list, factors_list, count):
    # Create a list of tuples of each number in nums_list and each number in factors_list
    products = [(i, j) for i in nums_list for j in factors_list]
    # Sort the list in descending order of the products
    products.sort(reverse=True)
    # Return the first count number of tuples from the sorted list
    return [i*j for i, j in products[:count]]