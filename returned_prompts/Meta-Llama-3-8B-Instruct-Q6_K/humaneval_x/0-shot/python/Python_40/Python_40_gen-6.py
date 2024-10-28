    # Check if list length is less than 3
    if len(l) < 3:
        return False

    # Create a set to store the numbers we have seen
    seen = set()

    # Iterate over the list
    for num in l:
        # Create a set to store the numbers that sum to -num
        to_see = set()

        # Iterate over the list again
        for other_num in l:
            # If the other number is not the same as the current number
            if other_num != num:
                # Calculate the third number
                third_num = -num - other_num
                # Check if we have seen this third number before
                if third_num in seen:
                    # If we have, return True
                    return True
                # Add the other number to the set of numbers we need to see
                to_see.add(other_num)
        # Add the current number to the set of numbers we have seen
        seen.add(num)

    # If we have iterated over the list and not found three numbers that sum to zero
    return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
    # return False
