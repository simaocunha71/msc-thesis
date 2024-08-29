def max_subarray_product(arr):
    max_end = min_end = result = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_end, min_end = min_end, max_end

        max_end = max(arr[i], max_end * arr[i])
        min_end = min(arr[i], min_end * arr[i])

        result = max(result, max_end)

    return result

print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))

"""
Explanation:

The function works by maintaining two variables max_end and min_end. 
max_end will keep track of the maximum product ending at the current position.
min_end will keep track of the minimum product ending at the current position 
because the product can become maximum if the next number is negative.

Then it iterates over the array. In each iteration, it first checks if the current number is negative. 
If it is, it swaps max_end and min_end because the product can become maximum if the next number is negative.

Then it updates max_end and min_end.
max_end is updated to be the maximum between the current number and max_end * current number.
min_end is updated to be the minimum between the current number and min_end * current number.

Finally, it updates result to be the maximum between the current result and max_end.

At the end of the function, it returns the result which is the maximum product subarray of the given array.
"""
<jupyter_output>
112
<jupyter_text>
**Problem 4**
<jupyter_code>
