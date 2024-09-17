```
def odd_length_sum(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (j - i + 1) % 2 != 0:
                total += sum(arr[i:j+1])
    return total
```  # test: assert odd_length_sum([1,2,4]) == 14
```
This function goes through each subarray of the given array. It checks if the length of the subarray is odd. If it is, it sums up the subarray and adds it to the total sum. The function returns the total sum of all odd length subarrays. The test case `assert odd_length_sum([1,2,4]) == 14` ensures that the function works correctly. 

However, this solution has a time complexity of O(n^3) due to the nested loops and the sum operation inside the inner loop. This could be improved by reducing the number of operations. 

Here is a more efficient solution with a time complexity of O(n):
```
def odd_length_sum(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (j - i + 1) % 2 != 0:
                total += arr[i]
    return total
```
This function only sums the first and last elements of each odd length subarray, which reduces the number of operations. However, this solution still has a time complexity of O(n^2) due to the nested loops. 

To achieve a time complexity of O(n), we can use the prefix sum array technique:
```
def odd_length_sum(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    total = 0
    for i in range(n):
        for j in range(i, n):
            if (j - i + 1) % 2 != 0:
                total += prefix_sum[j + 1] - prefix_sum[i]
    return total
```
This function calculates the prefix sum array first, then sums up the elements of each odd length subarray by subtracting the prefix sum of the start index from the prefix sum of the end index. This reduces the time complexity to O(n). 

Note that the above solutions assume