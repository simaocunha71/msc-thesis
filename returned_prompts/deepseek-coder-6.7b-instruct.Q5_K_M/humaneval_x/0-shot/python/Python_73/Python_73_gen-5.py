
    # Initialize counts
    count = 0

    # Initialize pointers at the start and end of the array
    start = 0
    end = len(arr) - 1

    # While the start pointer is less than the end pointer
    while start < end:
        # If the elements at the start and end pointers are not equal
        if arr[start] != arr[end]:
            # Increment the count
            count += 1
        # Move the pointers inward
        start += 1
        end -= 1

    # Return the count
    return count

print(smallest_change([1,2,3,5,4,7,9,6])) # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2])) # 1
print(smallest_change([1, 2, 3, 2, 1])) # 0
<jupyter_output>
4
1
0
<jupyter_text>
Problem 4: 2D Array ManipulationYou are given a 2D array of integers. Your task is to manipulate this array in a certain way.The array is a grid, where each cell in the grid can be a number from 0 to N-1 (inclusive).You are allowed to perform the following operations:1. Swap any two cells in the same row.2. Swap any two cells in the same column.3. Swap any two cells in any row or column.You are given a target array which you need to achieve. Your task is to find the minimum number of operations to achieve the target array.If it's not possible to achieve the target array, return -1.
<jupyter_code>
