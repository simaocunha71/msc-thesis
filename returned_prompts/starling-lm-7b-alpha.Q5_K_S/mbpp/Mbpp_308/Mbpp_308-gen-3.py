"""
def large_product(list1, list2, n):
    # Create an empty list to store the result
    result = []
    # Sort the two lists in descending order
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    # Iterate through the two lists and get the product of the first n elements of each list
    for i in range(n):
        result.append(list1[i] * list2[i])
    # Sort the result in descending order and return it
    result.sort(reverse=True)
    return result
"""

