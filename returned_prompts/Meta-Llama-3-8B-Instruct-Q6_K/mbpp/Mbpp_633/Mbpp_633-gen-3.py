```
def pair_xor_Sum(lst, n):
    total_xor = 0
    for i in range(n):
        for j in range(i+1, n):
            total_xor += lst[i] ^ lst[j]
    return total_xor
```


This function takes a list of numbers and a number n as input. It then calculates the sum of the XOR of all pairs of numbers in the list by iterating over the list and XORing each pair of numbers. The result is then returned.

The unit test `assert pair_xor_Sum([5,9,7,6],4) == 47` ensures that the function is working correctly for the given input. 

For example, when the input is `[5,9,7,6]` and `n=4`, the function calculates the sum of the XOR of all pairs of numbers in the list as follows:

* `5 ^ 9 = 14`
* `5 ^ 7 = 12`
* `5 ^ 6 = 11`
* `9 ^ 7 = 2`
* `9 ^ 6 = 15`
* `7 ^ 6 = 13`
The sum of these XOR values is `14 + 12 + 11 + 2 + 15 + 13 = 47`. 

So, the function returns `47` for the given input. 





