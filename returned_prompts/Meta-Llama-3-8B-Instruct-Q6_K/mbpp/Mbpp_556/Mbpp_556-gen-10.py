```
def find_Odd_Pair(arr, n):
    odd_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] ^ arr[j]) % 2 != 0:
                odd_pairs += 1
    return odd_pairs
```


The problem is asking to write a function that counts the number of pairs in a given array whose XOR value is odd. 

The function takes two parameters: an array of integers and a number (which is not used in this solution). 

The solution iterates over each pair of elements in the array and checks if the XOR of the pair is odd (i.e., if the remainder when divided by 2 is not 0). If the XOR is odd, it increments the count of odd pairs. 

The function returns the total count of odd pairs. 

The unit test `assert find_Odd_Pair([5,4,7,2,1],5) == 6` ensures that the function works correctly. 

For example, in the array [5,4,7,2,1], the pairs (5,4), (5,7), (5,2), (5,1), (4,7), and (4,2) have an odd XOR value, so the function should return 6. 