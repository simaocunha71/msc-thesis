def max_difference(pairs):
    # Convert the list of tuples into a list of differences
    differences = [abs(a - b) for a, b in pairs]
    # Return the maximum difference
    return max(differences)

