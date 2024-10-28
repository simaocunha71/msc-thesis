```
def pair_xor_Sum(lst, num):
    res = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            res += lst[i]^lst[j]
    return res
```


Explanation:
The problem is asking for a function that calculates the sum of the XOR operation of all pairs of numbers in the given list. The XOR operation is denoted by '^'. 

The unit test `assert pair_xor_Sum([5,9,7,6],4) == 47` suggests that the function should take two parameters: a list of numbers and the size of the list. In this case, the size of the list is 4, but it's not necessary as we can calculate it within the function.

The solution uses two nested loops to iterate over all pairs of numbers in the list, calculates the XOR of each pair and adds it to the result. The result is then returned.

Note: The XOR operation has the property that `a ^ b == b ^ a`, so we don't need to care about the order of the numbers in the pair. Also, `a ^ a == 0`, so we don't need to consider the same number with itself. These properties can be used to optimize the solution, but it's not necessary in this case. 