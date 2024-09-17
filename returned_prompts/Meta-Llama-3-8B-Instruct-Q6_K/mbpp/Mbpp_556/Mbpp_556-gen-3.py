```
def find_Odd_Pair(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i] ^ arr[j]) % 2 != 0:
                count += 1
    return count
```
This function takes an array and its length as input and returns the number of pairs whose xor value is odd. It does this by iterating over each pair of elements in the array, calculating the xor value, and checking if it is odd. If the xor value is odd, it increments the count. Finally, it returns the count. 

The unit test `assert find_Odd_Pair([5,4,7,2,1],5) == 6` ensures that the function is working correctly. In this case, the function should return 6 because there are 6 pairs with odd xor values. 

The time complexity of this function is O(n^2) because it has two nested loops that iterate over the array. The space complexity is O(1) because it only uses a constant amount of space to store the count and the indices. 





