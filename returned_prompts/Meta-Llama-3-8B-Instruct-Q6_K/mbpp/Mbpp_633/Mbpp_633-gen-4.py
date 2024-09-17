```
def pair_xor_Sum(lst,n):
    xor_sum = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            xor_sum += lst[i]^lst[j]
    return xor_sum
```


This function takes a list of numbers and an integer n as input, and returns the sum of XOR of all pairs of numbers in the list.

The unit test provided is:
```
assert pair_xor_Sum([5,9,7,6],4) == 47
```
This test case checks if the function correctly calculates the sum of XOR of all pairs of numbers in the list [5,9,7,6] and returns the expected result 47.

The function uses two nested loops to generate all pairs of numbers in the list, and for each pair, it calculates the XOR of the two numbers and adds it to the sum. The result is returned at the end of the function.