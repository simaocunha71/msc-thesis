def max_subarray_product(arr):
    n = len(arr)
    max_end_here = arr[0]
    min_end_here = arr[0]
    max_so_far = arr[0]
    for i in range(1, n):
        max_end_here = max(arr[i], max_end_here * arr[i], min_end_here * arr[i])
        min_end_here = min(arr[i], max_end_here * arr[i], min_end_here * arr[i])
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far

assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112


"""
Explanation:

The function max_subarray_product(arr) takes an array as input and returns the maximum product subarray.

In the function, we keep track of the maximum product ending at each position, the minimum product ending at each position, and the maximum product so far. 

For each element in the array, we update max_end_here and min_end_here based on the current element and the maximum and minimum product ending at the previous position. 

We also update max_so_far with the maximum of max_so_far and max_end_here. 

Finally, we return max_so_far as the maximum product subarray.

The time complexity of this function is O(n) where n is the length of the array. The space complexity is O(1) as it only uses a constant amount of space.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 5Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.Example:Input:[[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]Output:[1, 2, 3, 6, 9, 8, 7, 4, 5]
<