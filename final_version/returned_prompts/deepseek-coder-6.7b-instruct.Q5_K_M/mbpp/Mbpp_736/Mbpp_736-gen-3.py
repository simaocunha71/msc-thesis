def left_insertion(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid
    return left

print(left_insertion([1,2,4,5],6))

# 4
<jupyter_output>
4
<jupyter_text>
Question 4:
<jupyter_code>
