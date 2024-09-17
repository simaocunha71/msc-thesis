```
def find_Odd_Pair(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] ^ arr[j]) % 2 != 0:
                count += 1
    return count
```


Note: The function `find_Odd_Pair` takes two parameters, `arr` which is the list of elements and `n` which is the length of the list. It returns the number of pairs whose xor value is odd. The unit test `assert find_Odd_Pair([5,4,7,2,1],5) == 6` ensures that the function works correctly. The function uses two nested loops to generate all pairs of elements from the list, and then checks if the xor value of each pair is odd by using the modulus operator `%`. If the xor value is odd, it increments the count. Finally, it returns the count.