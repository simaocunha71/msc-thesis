```
def odd_length_sum(arr):
    total_sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if (j-i)%2 != 0:
                total_sum += sum(arr[i:j])
    return total_sum
```


This function iterates over all possible subarrays of the input array. For each subarray, it checks if the length is odd by using the condition `(j-i)%2 != 0`. If the length is odd, it adds the sum of the subarray to the total sum.

The unit test `assert odd_length_sum([1,2,4]) == 14` is used to verify the correctness of the function. It checks if the function returns the correct sum for the input array `[1,2,4]`. The expected output is `14`, which is the sum of all odd length subarrays of the input array.

The time complexity of this function is O(n^3), where n is the length of the input array. This is because we are iterating over all possible subarrays of the input array, and for each subarray, we are summing its elements. The space complexity is O(1), as we are using a constant amount of space to store the total sum and the subarray elements.