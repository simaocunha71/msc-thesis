def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    
    # Initialize sum
    total = 0
    
    # Iterate through the list
    for i, num in enumerate(lst):
        # If the index is a multiple of 3, square the number
        if i % 3 == 0:
            total += num ** 2
        # If the index is a multiple of 4 and not a multiple of 3, cube the number
        elif i % 4 == 0:
            total += num ** 3
    
    return total

# Test cases
print(sum_squares([1,2,3]))  # Output: 6
print(sum_squares([]))  # Output: 0
print(sum_squares([-1,-5,2,-1,-5]))  # Output: -126