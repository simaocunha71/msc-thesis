
def search(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] != arr[mid ^ 1]:
            high = mid
        else:
            low = mid + 1
    return arr[low]

print(search([1,1,2,2,3]))

"""
Explanation:
The main idea of this problem is to use Binary Search. Since the array is sorted and all the duplicate elements are grouped together, we can use Binary Search to find the element that appears only once.
The unique property of sorted array is that every element appears either twice or once.
When mid is even, if arr[mid] == arr[mid+1], it means the pair is not unique, and we need to look for the unique element on the right, so we update low = mid + 1. Otherwise, update high = mid.
When mid is odd, if arr[mid] == arr[mid-1], it means the pair is not unique, and we need to look for the unique element on the right, so we update low = mid + 1. Otherwise, update high = mid.
"""

# Time complexity: O(logn)
# Space complexity: O(1)

# Note: This solution assumes that the array contains only one element that appears once and all other elements appear at least twice. If the array has multiple elements appearing once and once, we would need to modify the solution to handle that.
<jupyter_output>
<empty_output>
<jupyter_text>
**Problem 2:**
<jupyter_code>
