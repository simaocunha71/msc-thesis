```
def find_Odd_Pair(lst, n):
    odd_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (lst[i] ^ lst[j]) % 2 != 0:
                odd_count += 1
    return odd_count
```
In this problem, we are asked to write a function that counts the number of pairs whose XOR value is odd. The function takes a list of integers and an integer as input, and returns the count of such pairs.

The unit test `assert find_Odd_Pair([5,4,7,2,1],5) == 6` helps in understanding the problem better. It means that for the given list [5,4,7,2,1] and the size of the list (5), the function should return 6, which is the correct count of pairs whose XOR value is odd.

The solution to the problem is a simple loop that iterates over the list and checks the XOR value of each pair. If the XOR value is odd, it increments the count. Finally, it returns the count.

The time complexity of this solution is O(n^2) because it has a nested loop structure. The space complexity is O(1) because it only uses a constant amount of space to store the count. 





