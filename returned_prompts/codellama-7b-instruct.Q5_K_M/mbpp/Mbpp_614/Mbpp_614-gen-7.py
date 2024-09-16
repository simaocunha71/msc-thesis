"""
def cummulative_sum(tuple_list):
    # Initialize an empty list to store the cummulative sum
    cummulative_list = []
    # Iterate through the tuple list
    for element in tuple_list:
        # Initialize an empty list to store the sum of the current element
        sum_of_element = []
        # Iterate through the elements of the current element
        for num in element:
            # Add the current element to the sum of the current element
            sum_of_element.append(num)
        # Append the sum of the current element to the cummulative list
        cummulative_list.append(sum(sum_of_element))
    # Return the cummulative list
    return cummulative_list
"""