```
def find_kth(arr1, arr2, k):
    if not arr1:
        return arr2[k - 1]
    if not arr2:
        return arr1[k - 1]
    if k == 1:
        return min(arr1[0], arr2[0])
    i, j = (k // 2) - 1, (k // 2) - 1
    if arr1[i + 1] < arr2[j + 1]:
        return find_kth(arr1[i + 1:], arr2, k - i - 1)
    elif arr2[j + 1] < arr1[i + 1]:
        return find_kth(arr1, arr2[j + 1:], k - j - 1)
    else:
        return arr1[i + 1]
```


Explanation:
This function finds the kth element in two sorted arrays. If one array is empty, it returns the kth element from the other array. If k is 1, it returns the minimum of the first elements from both arrays. If k is greater than 1, it finds the middle elements from both arrays and compares them. If the middle element from the first array is smaller, it recursively calls the function with the rest of the first array and k reduced by the index of the middle element. If the middle element from the second array is smaller, it recursively calls the function with the rest of the second array and k reduced by the index of the middle element. If the middle elements are equal, it returns the middle element from the first array. The time complexity of this function is O(log(min(k, n1, n2))), where n1 and n2 are the lengths of the two arrays. The space complexity is O(log(min(k, n1, n2))), as the function calls itself recursively.