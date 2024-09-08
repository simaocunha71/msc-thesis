def last(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1

print(last([1,2,3],1))

# 0

# 1. The function last is defined with two parameters arr and target.
# 2. The loop starts from the last element of the list and goes till the first element.
# 3. If the target element is found, it returns the index.
# 4. If the target element is not found, it returns -1.

# Time complexity of the function is O(n), where n is the length of the list.
# Because in the worst case scenario, the function has to iterate through the entire list.
# Space complexity is O(1) as no additional space is being used.

# Note: The given list is sorted. If the list is not sorted, we can use the binary search algorithm which will make the time complexity O(log n).
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
