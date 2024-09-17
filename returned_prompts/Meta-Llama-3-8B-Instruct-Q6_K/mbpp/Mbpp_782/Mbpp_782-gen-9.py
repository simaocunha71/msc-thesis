```
def odd_length_sum(arr):
    total_sum = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            if j - i == 1:
                continue
            if (j - i) % 2 != 0:
                total_sum += sum(arr[i:j])
    return total_sum
```


The problem asks to find the sum of all odd length subarrays in a given array. 

The provided unit test `assert odd_length_sum([1,2,4]) == 14` helps to understand the problem better. It means the sum of all odd length subarrays in the array [1,2,4] is 14.

The function `odd_length_sum` takes an array as an input. It initializes a variable `total_sum` to store the sum of all odd length subarrays. Then it iterates over the array using two nested loops. The outer loop `i` represents the start of the subarray and the inner loop `j` represents the end of the subarray. 

It checks if the length of the subarray is odd by using the condition `(j - i) % 2 != 0`. If the length is odd, it adds the sum of the subarray to `total_sum`. The function finally returns the `total_sum`.

This solution has a time complexity of O(n^2) due to the nested loops. It is not efficient for large inputs. A more efficient solution could be achieved by using a single loop and calculating the sum of each subarray on the fly, but it would be more complex to implement. 





Python code:

```
def odd_length_sum(arr):
    total_sum = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            if j - i == 1:
                continue
            if (j - i) % 2 != 0:
                total_sum += sum(arr[i:j])
    return total_sum
```
This function takes an array as input and returns the sum of all odd length subarrays. It has a time complexity of O(n^2) due to the nested loops. It is not efficient for large inputs. A more efficient solution could be achieved by using a single loop and calculating the sum of each subarray on the fly, but it would be more complex to implement. 

The unit test `assert odd_length_sum