def check_greater(arr, num):
    # Traverse through the array
    for i in arr:
        # If any element is found to be less than num
        if i < num:
            return False
    return True