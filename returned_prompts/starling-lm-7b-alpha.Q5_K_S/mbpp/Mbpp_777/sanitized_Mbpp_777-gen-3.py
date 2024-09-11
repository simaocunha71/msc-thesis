def find_sum(lst):
    # Create a set from the given list
    set_lst = set(lst)
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the set
    for i in set_lst:
        sum += i
    return sum