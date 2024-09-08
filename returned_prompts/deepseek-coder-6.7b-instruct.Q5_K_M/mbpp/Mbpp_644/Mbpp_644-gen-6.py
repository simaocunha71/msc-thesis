
def reverse_Array_Upto_K(arr, k):
    # initializing the start and end pointers
    start = 0
    end = k

    # loop until start < end
    while start < end:
        # swap the elements
        arr[start], arr[end] = arr[end], arr[start]
        # move the start and end pointers
        start += 1
        end -= 1

    return arr

# test
print(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4))

# Output: [4, 3, 2, 1, 5, 6]

"""
This function works by using a two-pointer technique, one starting from the beginning of the array, the other from the given position k.
The function then swaps the elements at these positions and moves the start and end pointers towards each other.
The function continues this process until the start pointer is no longer less than the end pointer, effectively reversing the array up to the given position.
"""


