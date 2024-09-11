def find_min_diff(arr, num):
    arr = sorted(arr)
    min_diff = float('inf')
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] < min_diff:
            min_diff = arr[i+1] - arr[i]
    return min_diff


# Python3 program to find
# minimum difference between
# any two elements in a given
# array. 

# Function to find minimum
# difference between any two
# elements in a given array
def find_min_diff(arr, num):
    # Sorting the given array
    arr.sort()

    # Initialize minimum
    # difference value as Infinity
    min_diff = float('inf')

    # Traverse array from
    # beginning to end
    for i in range(len(arr) - 1):
        # If the difference
        # between current
        # and next element
        # is less than
        # minimum difference
        # then update it
        if (arr[i + 1] - arr[i]) < min_diff:
            min_diff = (arr[i + 1] - arr[i])

    # Return the minimum
    # difference
    return min_diff

# Driver code
arr = [1,5,3,19,18,25]
num = 6
print(find_min_diff(arr, num))

# This code is contributed by
# Sanjeev Kumar Singh(SUGO)




# Python3 program to find
# minimum difference between
# any two elements in a given
# array. 

# Function to find minimum
# difference between any two
# elements in a given array
def find_min_diff(arr, num):
    # Sorting the given array
    arr.sort()

    # Initialize minimum
    # difference value as Infinity
    min_diff = float('inf')

    # Traverse array from
    # beginning to end
    for i in range(len(arr) - 1):
        # If the difference
        # between current
        # and next element
        # is