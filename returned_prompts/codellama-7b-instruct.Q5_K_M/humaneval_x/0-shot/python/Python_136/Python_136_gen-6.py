
    # Check the type of the input list
    if type(lst) != list:
        raise ValueError("Input must be a list.")

    # Check the length of the input list
    if len(lst) == 0:
        return (None, None)

    # Check the type of the elements in the list
    for i in range(len(lst)):
        if type(lst[i]) != int:
            raise ValueError("List elements must be integers.")

    # Initialize the largest and smallest variables
    largest, smallest = None, None

    # Iterate over the list and find the largest and smallest integers
    for i in range(len(lst)):
        if lst[i] < 0 and (largest == None or lst[i] > largest):
            largest = lst[i]
        elif lst[i] > 0 and (smallest == None or lst[i] < smallest):
            smallest = lst[i]

    # Return the tuple of (largest, smallest)
    return (largest, smallest)
