def count_element_in_list(lst, element):
    return sum(1 for sublist in lst if element in sublist)  # use a list comprehension to count the number of sublists containing the element
    # or use a regular for loop for better readability
    # count = 0
    # for sublist in lst:
    #     if element in sublist:
    #         count += 1
    # return count