    # Create a list of all elements in arr
    elements = list(arr)

    # Sort the list in descending order
    elements.sort(reverse=True)

    # Return the first k elements of the sorted list
    return elements[:k]

