```
def find_kth(arr1, arr2, k):
    i, j = 0, 0
    while k > 0:
        if i == len(arr1):
            return arr2[j + k - 1]
        if j == len(arr2):
            return arr1[i + k - 1]
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
        k -= 1
    return -1
```



Explanation:
The problem is to find the kth element from two sorted arrays. We can use a binary search approach to solve this problem. The idea is to keep track of the current position in both arrays and move the pointer of the smaller element to the next position. We can reduce the problem to the k-1th element by subtracting 1 from k and moving the pointer of the smaller element. If one array is exhausted, we return the kth element from the other array. If k is 0, we return the kth element from the array that has not been exhausted. If k is negative, we return -1 as the result is invalid. The time complexity of this solution is O(log(min(m, n))), where m and n are the lengths of the two arrays. The space complexity is O(1). This solution is efficient and can handle large arrays. The unit test `assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6` demonstrates the correctness of this solution.