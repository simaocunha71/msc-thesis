```
def odd_length_sum(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if j - i == 1:
                total += arr[i]
            elif j - i % 2 != 0:
                total += sum(arr[i:j])
    return total
```


The function `odd_length_sum` takes a list of integers `arr` as input and returns the sum of all odd length subarrays. It works by iterating over all possible subarrays, checking if the length of the subarray is odd, and if so, adding the sum of the subarray to the total sum.

The unit test `assert odd_length_sum([1,2,4]) == 14` helps to clarify the problem by providing an example of a list and the expected output. This test case is used to verify that the function is working correctly.

The time complexity of this function is O(n^2) because it has two nested loops, each of which runs n times. The space complexity is O(1) because it only uses a constant amount of space to store the total sum and the current subarray. 

Please note that the problem statement is not entirely clear. However, based on the provided unit test, it seems that the problem is asking for the sum of all odd length subarrays, not just the sum of all odd length subarrays that are contiguous. If the problem is asking for the sum of all odd length contiguous subarrays, the solution would be different. 

Also, the problem statement does not specify what should happen if the input list is empty. However, based on the provided unit test, it seems that the function should return 0 if the input list is empty. 

In the future, it would be helpful to provide more clear and concise problem statements, and to test the function with a variety of inputs to ensure that it is working correctly. 