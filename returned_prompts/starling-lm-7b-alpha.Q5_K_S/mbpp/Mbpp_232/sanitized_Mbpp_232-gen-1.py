def larg_nnum(num_list, n):
    # Sort list in descending order
    sorted_list = sorted(num_list, reverse=True)
    # Return the first n largest numbers
    return sorted_list[:n]