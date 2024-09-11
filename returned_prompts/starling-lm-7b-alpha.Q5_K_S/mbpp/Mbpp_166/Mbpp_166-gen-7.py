```
def find_even_pair(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i+1,n):
            if (nums[i] ^ nums[j]) % 2 == 0:
                res += 1
    return res
```

This function uses two nested loops to iterate through each pair of integers in the given list. It checks if the XOR of the two integers results in an even number by using the modulus operator (%). If the XOR is even, the function increments the result count. Finally, the function returns the total number of even XOR pairs found in the list.

For the provided example, the function will return 4, as there are four pairs of integers in the list [5, 4, 7, 2, 1] that XOR to an even number: (5, 4), (5, 7), (5, 2), and (5, 1).

The time complexity of this solution is O(n^2), where n is the length of the input list. This is because there are two nested loops, each iterating through the entire list for each iteration of the other loop. The space complexity is O(1) as the solution does not require any additional memory beyond the input list and the result variable.

Overall, this solution provides an efficient way to count the number of pairs of integers in a list that XOR to an even number.

```python
def find_even_pair(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i+1,n):
            if (nums[i] ^ nums[j]) % 2 == 0:
                res += 1
    return res
```

To use this function, you can pass a list of integers to it, and it will return the count of pairs that XOR to an even number. For example, if you call `find_even_pair([5, 4, 7, 2, 1])`, it will return 4, indicating that there are four pairs of integers in the