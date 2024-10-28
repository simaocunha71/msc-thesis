```
def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    if n == 2:
        return m * (m - 1) // 2
    
    total = 0
    for i in range(2, m):
        total += get_total_number_of_sequences(m, n - 1)
    return total
```


This function uses recursion to solve the problem. It starts by considering the base cases where n is 1 or 2, and then recursively calculates the total number of possible sequences for larger values of n. The function returns the total number of possible sequences.

The unit test `assert get_total_number_of_sequences(10, 4) == 4` suggests that the function should return the number of possible sequences, not the sequences themselves. Therefore, the function only needs to calculate the total number of possible sequences without generating them. This makes the problem more manageable and efficient.

Note that the time complexity of this function is exponential, which may not be suitable for large values of n. A more efficient solution would be to use dynamic programming to calculate the total number of possible sequences in O(m*n) time. However, the recursive solution is simple and easy to understand, making it a good choice for small values of n.