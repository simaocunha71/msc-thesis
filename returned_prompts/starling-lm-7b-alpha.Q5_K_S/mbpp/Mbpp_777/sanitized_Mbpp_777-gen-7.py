def find_sum(lst):
    # Create an empty set to store the non-repeated elements
    unique_set = set()

    # Iterate through the list and add each element to the set
    for elem in lst:
        unique_set.add(elem)

    # Convert the set to a list and calculate the sum
    return sum(unique_set)