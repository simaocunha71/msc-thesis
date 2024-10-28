```
def find_Odd_Pair(lst,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if bin(lst[i]^lst[j]).count('1')%2!=0:
                count+=1
    return count
```
In this problem, we need to count the number of pairs in the given list whose xor value is odd.

The given list is `[5,4,7,2,1]` and the size of the list is `5`. 

The unit test for this function is `assert find_Odd_Pair([5,4,7,2,1],5) == 6`. 

This unit test means that the function should return `6` when the input is the given list and the size of the list is `5`.

In the function, we use two nested for loops to generate all pairs of elements from the list. For each pair, we calculate the xor value and check if the number of `1`s in the binary representation of the xor value is odd. If it is, we increment the count.

Finally, we return the count. 

The time complexity of this function is O(n^2) because we are using two nested for loops. The space complexity is O(1) because we are not using any extra space that scales with the input size. 