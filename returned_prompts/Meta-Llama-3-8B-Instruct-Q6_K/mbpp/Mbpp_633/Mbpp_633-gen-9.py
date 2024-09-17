```
def pair_xor_Sum(lst, n):
    xor_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            xor_sum += lst[i] ^ lst[j]
    return xor_sum
```


The function `pair_xor_Sum` takes a list `lst` and an integer `n` as input. It calculates the sum of XOR of all pairs of numbers in the list. The function uses two nested loops to generate all pairs of numbers in the list and then calculates the XOR of each pair using the bitwise XOR operator `^`. The sum of all these XOR values is returned as the result. 

For example, the unit test `assert pair_xor_Sum([5,9,7,6],4) == 47` passes because the XOR of all pairs of numbers in the list `[5,9,7,6]` is indeed 47. 

The time complexity of this function is O(n^2) because it uses two nested loops to generate all pairs of numbers in the list. The space complexity is O(1) because it only uses a constant amount of space to store the sum of XOR values. 