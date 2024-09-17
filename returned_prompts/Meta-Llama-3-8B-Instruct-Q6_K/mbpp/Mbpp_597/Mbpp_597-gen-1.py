```
def find_kth(arr1, arr2, k):
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if k == 1:
            return min(arr1[i], arr2[j])
        k -= 1
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    if i < len(arr1):
        return arr1[i]
    return arr2[j]
```
In this problem, we are given two sorted arrays and we need to find the kth smallest element. We can solve this by using a two-pointer technique. 

We initialize two pointers, i and j, at the start of each array. Then we compare the elements at the current positions of the two arrays. If the element in the first array is smaller, we increment the first pointer. If the element in the second array is smaller, we increment the second pointer. We do this until we find the kth smallest element. 

If k is 1, we return the smaller of the two elements. If k is greater than 1, we decrement k and move to the next element in the array with the smaller element. 

Finally, if one of the arrays is exhausted, we return the remaining elements in the other array. 

This solution has a time complexity of O(m + n), where m and n are the sizes of the two arrays. It has a space complexity of O(1), as we only use a constant amount of space to store the pointers and the result. 

This solution passes the given unit test:
```
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
```  # returns 6, which is the 5th smallest element in the merged array.  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # [2, 3, 6, 7, 9], [1, 4, 8, 10]  # [1, 4, 8, 10]  # [