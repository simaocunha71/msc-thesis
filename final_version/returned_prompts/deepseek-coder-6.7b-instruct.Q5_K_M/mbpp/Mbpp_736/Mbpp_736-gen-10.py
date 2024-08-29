def left_insertion(arr, key):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left

print(left_insertion([1,2,4,5],6)) # 4

"""
Explanation:
The function uses binary search to find the left insertion point. It starts by setting two pointers, left and right, to the beginning and the end of the array, respectively. It then enters a loop that continues until left is not less than right. In each iteration of the loop, it calculates the middle index, mid. If the middle element is less than the key, it updates left to be mid + 1. Otherwise, it updates right to be mid. The loop continues until left is not less than right. At the end of the loop, left will be the index of the left insertion point.
"""
<jupyter_output>
4
<jupyter_text>
