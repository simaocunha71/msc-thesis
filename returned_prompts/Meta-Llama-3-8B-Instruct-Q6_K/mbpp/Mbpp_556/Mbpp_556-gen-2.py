```
def find_Odd_Pair(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i] ^ arr[j]) % 2 != 0:
                count += 1
    return count
```


This function takes an array and its size as input and returns the count of pairs whose xor value is odd. The function uses two nested loops to generate all possible pairs from the array. For each pair, it calculates the xor value and checks if it is odd (i.e., remainder when divided by 2 is 1). If the xor value is odd, it increments the count. Finally, it returns the count.

The unit test `assert find_Odd_Pair([5,4,7,2,1],5) == 6` ensures that the function works correctly. It checks that for the array [5,4,7,2,1] with size 5, the function returns 6, which is the correct count of pairs with odd xor value. 

This function has a time complexity of O(n^2), where n is the size of the array. This is because it uses two nested loops to generate all possible pairs from the array. This may not be efficient for large arrays. A more efficient solution could be to use a single loop and a hash set to keep track of the elements that have been seen so far, and then calculate the xor value for each element with the elements in the hash set. This would reduce the time complexity to O(n).  However, the problem statement does not require this level of optimization, and the provided solution is simple and easy to understand. 