def split_Arr(arr, n):
    # Split the list at the nth element
    first_part = arr[:n]
    second_part = arr[n:]

    # Add the first part to the end of the second part
    result = second_part + first_part

    return result

# Test the function
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]

# Define a helper function to add a value to an array
def add_value(arr, value):
    arr.append(value)
    return arr

# Define a function to rotate an array by a certain number of steps
def rotate_Array(arr, steps):
    # Add the first part of the array to the end of the second part
    rotated_arr = split_Arr(arr, steps)

    # Add the steps-th element to the start of the array
    rotated_arr = add_value(rotated_arr, arr[steps-1])

    return rotated_arr

# Test the function
assert rotate_Array([1,2,3,4,5], 2) == [2,3,4,5,1]

# Define a function to rotate an array to the left
def rotate_Array_left(arr, steps):
    # Add the last part of the array to the start of the second part
    rotated_arr = split_Arr(arr, steps)

    # Add the steps-th element to the end of the array
    rotated_arr = add_value(rotated_arr, arr[steps-1])

    return rotated_arr

# Test the function
assert rotate_Array_left([1,2,3,4,5], 2) == [3,4,5,1,2]

# Define a function to rotate an array to the left by a certain number of steps
def rotate_Array_left_steps(arr, steps):
    # Add the steps-th element to the start of the array
    rotated_arr = add_value(arr, arr[steps