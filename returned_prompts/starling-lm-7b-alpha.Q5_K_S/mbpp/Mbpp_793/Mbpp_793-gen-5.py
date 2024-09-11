def last(arr,key):
    low,high = 0,len(arr)-1
    while low<high:
        mid = (low+high)//2
        if arr[mid]>key:
            high = mid-1
        elif arr[mid]<key:
            low = mid+1
        else:
            low = mid
    if arr[low]!=key:
        return -1
    return low

# Test Cases
print(last([1,2,3],1)) # 0
print(last([1,2,3],2)) # 1
print(last([1,2,3],3)) # 2
print(last([1,2,3],4)) # -1

"""
The time complexity of this function is O(log n) in average and worst case,
since in each iteration we are reducing the array size by half.

The space complexity is O(1) as we are not using any extra space.
"""

# If you have any doubt or suggestions regarding the above code, please feel free to comment.

"""
If the array is not sorted, you can first sort the array and then apply binary search.
The time complexity of sorting an array is O(n log n) using built-in Python functions like sorted().
After sorting, you can use binary search to find the last position of the element in the sorted array.
The time complexity of binary search is O(log n).

Here is an implementation of the above approach:
"""

def last_unsorted(arr,key):
    arr.sort()
    low,high = 0,len(arr)-1
    while low<high:
        mid = (low+high)//2
        if arr[mid]>key:
            high = mid-1
        elif arr[mid]<key:
            low = mid+1
        else:
            low = mid
    if arr[low]!=key:
        return -1
    return low

# Test Cases
print(last_unsorted([1,2,3],1)) # 0
print(last_unsorted([1,2,3],2)) # 1
print(last_unsorted([