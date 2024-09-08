def left_insertion(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

print(left_insertion([1,2,4,5],6))
<jupyter_output>
4
<jupyter_text>
Problem 3: Binary Search
<jupyter_code>
