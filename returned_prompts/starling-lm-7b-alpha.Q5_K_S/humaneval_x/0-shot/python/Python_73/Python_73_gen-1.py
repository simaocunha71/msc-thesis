    # Initialize count to 0
    count = 0
    # Create a set to store seen elements
    seen = set()
    # Iterate over the array from the left and the right side
    while arr:
        # Take the first element from the left
        left = arr.pop(0)
        # Take the last element from the right
        right = arr.pop()
        # If the elements are equal, continue
        if left == right:
            continue
        # If the elements are not equal and one of them has already been seen, increment the count
        if left in seen or right in seen:
            count += 1
        # Otherwise, add both elements to the seen set
        else:
            seen.add(left)
            seen.add(right)
    # Return the count
    return count

# Test cases
print(smallest_change([1,2,3,5,4,7,9,6])) # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2])) # 1
print(smallest_change([1, 2, 3, 2, 1])) # 0












































































































































































































































