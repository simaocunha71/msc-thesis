from functools import reduce
def large_product(list1, list2, n):
    # Sort both the lists and select the largest element from each list
    list1.sort(reverse=True)
    list2.sort(reverse=True)

    # Select the first n elements from each list
    list1 = list1[:n]
    list2 = list2[:n]

    # Compute the product of all the elements in each list
    prod1 = reduce(lambda x, y: x*y, list1)
    prod2 = reduce(lambda x, y: x*y, list2)

    # Return the top n products
    return [prod1, prod2]