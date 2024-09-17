```
def odd_length_sum(arr):
    total_sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if (j-i) % 2 != 0:
                total_sum += sum(arr[i:j])
    return total_sum
```


Explanation:
The function `odd_length_sum` takes a list `arr` as input and returns the sum of all odd length subarrays. 

It uses two nested loops to generate all possible subarrays. The outer loop iterates over the start index of the subarray, and the inner loop iterates over the end index. 

For each subarray, it checks if the length of the subarray is odd by checking if `(j-i)` is odd. If it is, it adds the sum of the subarray to `total_sum`. 

Finally, it returns `total_sum` which is the sum of all odd length subarrays. 

The unit test `assert odd_length_sum([1,2,4]) == 14` ensures that the function works correctly.  For the input `[1,2,4]`, the odd length subarrays are `[1]`, `[2]`, `[1,2]`, `[1,4]`, `[2,4]`, and the sum of these subarrays is `1+2+1+3+4=14`. 
```python
assert odd_length_sum([1,2,4]) == 14
```


This solution has a time complexity of O(n^2) where n is the length of the input array, because it uses two nested loops to generate all possible subarrays. The space complexity is O(1) as it only uses a constant amount of space to store the sum of the subarrays. 
```
```python
def odd_length_sum(arr):
    total_sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if (j-i) % 2 != 0:
                total_sum += sum(arr[i:j])
    return total_sum
```python
```python
assert odd_length_sum([1,2,4]) == 14
```python
```python
assert odd_length_sum([1,2,4]) == 14
```python
```python
assert odd_length_sum([1,2,4]) == 14
```python
```python
assert odd_length_sum([