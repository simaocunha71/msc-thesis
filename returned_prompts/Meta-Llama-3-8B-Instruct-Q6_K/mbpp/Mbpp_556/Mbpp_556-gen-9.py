```
def find_Odd_Pair(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]^arr[j])%2 != 0:
                count+=1
    return count
```
The function `find_Odd_Pair` takes a list of integers `arr` and an integer `n` as input and returns the count of pairs in the list whose XOR value is odd.

The function iterates over the list using two nested loops to generate all pairs of elements. For each pair, it checks if the XOR value is odd by using the modulo operator `%`. If the remainder is not zero (i.e., the XOR value is odd), it increments the count.

The unit test `assert find_Odd_Pair([5,4,7,2,1],5) == 6` ensures that the function works correctly for the given input. In this case, the function should return 6, which is the correct count of pairs with odd XOR values.