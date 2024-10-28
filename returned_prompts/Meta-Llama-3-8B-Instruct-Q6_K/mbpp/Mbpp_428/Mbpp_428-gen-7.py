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
The shell sort function sorts the array by repeatedly taking a gap and sorting the array with the gap, then reducing the gap until it is 0. It starts with a gap equal to half of the array length, then reduces it by half until it is 0. This process is repeated until the array is sorted. The function returns the sorted array.    
The unit test `assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]` checks that the function correctly sorts the array.    
This solution has a time complexity of O(n log n) and a space complexity of O(1), making it efficient for large arrays.    
However, the shell sort algorithm is not a stable sort, meaning that equal elements may be swapped during the sorting process. This can be a problem if the array contains equal elements that should maintain their original order.    
To make the shell sort algorithm stable, you can use a variation of the algorithm that uses insertion sort for the inner loop, which is a stable sort. This would increase the time complexity to O(n^2) in the worst case, but it would ensure that equal elements maintain their original order.    
In this solution, the inner loop uses a temporary variable to store the current element, and then shifts the elements in the array to make room for the current element. This process is repeated until the correct position for the current element is found. The function returns the sorted array.    
The unit test `assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]` checks that the function correctly sorts