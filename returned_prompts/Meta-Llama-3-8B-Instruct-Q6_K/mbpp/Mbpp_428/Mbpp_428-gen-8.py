```
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr
```



Explanation:
The shell sort algorithm is a variation of the insertion sort algorithm. It is a non-comparative sorting algorithm that works by dividing the array into sub-arrays and sorting them individually. The algorithm starts with a gap of half the size of the array and reduces it by half in each iteration until it reaches 1. 

In this implementation, we start with a gap of half the size of the array and iterate through the array. For each element, we compare it with the elements at the gap distance before it and shift them to the right until we find the correct position for the current element. 

We repeat this process until the gap becomes 1, at which point the array is sorted. The function returns the sorted array. 

The unit test `assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]` ensures that the function works correctly. 

The time complexity of shell sort is O(n log n) on average, although it can be O(n^2) in the worst case if the gap sequence is chosen poorly. The space complexity is O(1) as we are not using any extra space. 





Please note that this is a basic implementation of the shell sort algorithm. There are many ways to improve it, such as using a more efficient gap sequence or using insertion sort for small sub-arrays. However, this implementation should work correctly for most cases.