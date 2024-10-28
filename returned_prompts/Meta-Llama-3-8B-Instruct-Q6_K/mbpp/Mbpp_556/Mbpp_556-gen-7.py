```
def find_Odd_Pair(arr, n):
    odd_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] ^ arr[j]) % 2 != 0:
                odd_pairs += 1
    return odd_pairs
```


This function iterates through all pairs of elements in the given array and checks if the XOR operation of the pair is odd. If it is, it increments the count of odd_pairs. Finally, it returns the total count of odd_pairs. The unit test provided ensures that the function works correctly for the given array and the size of the array. 





