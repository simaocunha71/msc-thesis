```
def find_kth(arr1, arr2, k):
    if k == 1:
        return min(arr1[0], arr2[0])
    idx1, idx2 = 0, 0
    while k > 1:
        if idx1 + 1 >= len(arr1):
            return arr2[k - 1]
        if idx2 + 1 >= len(arr2):
            return arr1[k - 1]
        if arr1[idx1] < arr2[idx2]:
            k -= 1
            idx1 += 1
        else:
            k -= 1
            idx2 += 1
    if k == 1:
        if arr1[idx1] < arr2[idx2]:
            return arr1[idx1]
        else:
            return arr2[idx2]
    if idx1 + 1 >= len(arr1):
        return arr2[idx2]
    if idx2 + 1 >= len(arr2):
        return arr1[idx1]
    if arr1[idx1] < arr2[idx2]:
        return arr1[idx1 + 1]
    else:
        return arr2[idx2 + 1]
```
The problem is asking to find the kth element from two sorted arrays. We can solve this problem by using a two-pointer approach. We start by comparing the smallest elements of the two arrays. If the smallest element is from the first array, we decrement k by 1 and move the pointer to the next element in the first array. If the smallest element is from the second array, we decrement k by 1 and move the pointer to the next element in the second array. We repeat this process until k becomes 1.

If k becomes 1, it means we have found the kth element. If k is greater than the length of the first array, it means the kth element is in the second array. If k is greater than the length of the second array, it means the kth element is in the first array. If k is equal to the length of the first array, it means the kth element is the last element of the second array. If k is equal to the length of the second array, it means the kth element is the last element of the first array.

The unit test `assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 