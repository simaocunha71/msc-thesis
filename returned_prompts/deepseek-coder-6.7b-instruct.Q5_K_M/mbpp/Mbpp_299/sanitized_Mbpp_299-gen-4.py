def max_aggregate(lst):
    # Creating an empty dictionary
    d = {}
    # For each tuple in the list
    for name, num in lst:
        # If the name is not in the dictionary, add it with the number as value
        if name not in d:
            d[name] = num
        # If the name is already in the dictionary, add the number to the current value
        else:
            d[name] += num
    # Get the maximum value in the dictionary
    max_value = max(d.values())
    # Get the key corresponding to the maximum value
    max_key = [k for k, v in d.items() if v == max_value]
    # Return the tuple with the maximum value
    return (max_key[0], max_value)