def large_product(list1, list2, n):
    """Returns the top n largest products of one element from each list.

    Arguments:
    list1 - a list of positive integers
    list2 - a list of positive integers
    n - an integer

    Returns:
    A list of the n largest products
    """
    # Sort both lists in descending order
    list1.sort(reverse=True)
    list2.sort(reverse=True)

    # Initialize the result list
    result = []

    # Generate the largest products
    for i in range(n):
        result.append(list1[i] * list2[i])

    # Return the result
    return result