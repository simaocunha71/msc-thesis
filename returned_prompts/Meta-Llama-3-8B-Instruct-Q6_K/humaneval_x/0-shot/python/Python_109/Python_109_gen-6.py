    # check if array is empty
    if not arr:
        return True

    # initialize a flag to track if array can be sorted
    can_sort = True

    # initialize a variable to store the smallest element so far
    smallest = arr[0]

    # iterate over the array
    for num in arr[1:]:
        # if the current number is smaller than the smallest number seen so far
        if num < smallest:
            # set the flag to False
            can_sort = False
            # break the loop
            break
        # update the smallest number seen so far
        smallest = num

    # if the flag is True, return True
    if can_sort:
        return True
    # otherwise, return False
    return False

# Test cases
print(move_one_ball([3, 4, 5, 1, 2])) # True
print(move_one_ball([3, 5, 4, 1, 2])) # False
print(move_one_ball([])) # True
print(move_one_ball([5])) # True
print(move_one_ball([5, 4])) # True
print(move_one_ball([5, 4, 3, 2, 1])) # True
print(move_one_ball([5, 3, 4, 2, 1])) # False
print(move_one_ball([5, 4, 3, 1, 2])) # True
print(move_one_ball([5, 1, 4, 2, 3])) # True
print(move_one_ball([5, 2, 4, 1, 3])) # True
print(move_one_ball([5, 3, 1, 4, 2])) # True
print(move_one_ball([5, 1, 2, 3, 4])) # True
print(move_one_ball([5, 4, 3, 2, 1, 0])) # True
print(move_one_ball([5, 3, 4, 2, 1, 0])) # True
print(move_one_ball([5, 4, 3, 1, 2, 0])) # True
print(move_one_ball([5, 1, 4, 2, 3, 0])) # True
print(move_one_ball([5, 2, 4, 1,