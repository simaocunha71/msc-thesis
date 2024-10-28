The Lucas sequence is a sequence of integers in which each term is the sum of the two preceding terms, starting from 2 and 1. The function to find the n'th Lucas number is given as follows:

```Python
def find_lucas(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a + b
        return b
```

This function uses a loop to calculate the n'th Lucas number. If n is 1 or 2, it returns 1 or 2 respectively. For n greater than 2, it initializes two variables a and b to 1 and 2, then iteratively updates a and b to b and a + b respectively, until n - 1 iterations. Finally, it returns b which is the n'th Lucas number. 

For example, find_lucas(9) returns 76. 76 is the 9th Lucas number. 

This function is efficient for calculating the n'th Lucas number because it uses a loop that runs in O(n) time, and it only requires a constant amount of space to store the variables a and b. Therefore, its time complexity is O(n) and its space complexity is O(1). 