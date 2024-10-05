
def search(lst):
    # check if the list is empty
    if not lst:
        return -1
    # sort the list and reverse it
    lst.sort(reverse=True)
    # initialize the max value
    max_value = -1
    # initialize the max frequency
    max_frequency = -1
    # iterate through the list
    for element in lst:
        # check if the element is greater than 0
        if element > 0:
            # if the element frequency is greater than or equal to the element value
            if lst.count(element) >= element:
                # update the max value
                max_value = element
                # update the max frequency
                max_frequency = lst.count(element)
    # return the max value if it's greater than -1
    if max_frequency >= max_value:
        return max_value
    else:
        return -1


