def find_sum(l):
    # Create a set from the given list
    s = set(l)
    # Initialize sum to 0
    sum = 0
    # Iterate over the set and add each element to the sum
    for i in s:
        sum += i
    # Return the sum
    return sum