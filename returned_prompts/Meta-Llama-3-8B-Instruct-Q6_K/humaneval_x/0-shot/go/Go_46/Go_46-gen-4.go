The Fib4 number sequence can be efficiently computed using dynamic programming. The idea is to precompute and store the values of the sequence for smaller values of n and then use these values to compute the value of the sequence for larger values of n.

Here is a Python implementation of the Fib4 function:
```
def Fib4(n):
    if n <= 3:
        return [0, 0, 2, 0][n-1]
    fib4 = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib4.append(fib4[i-1] + fib4[i-2] + fib4[i-3] + fib4[i-4])
    return fib4[n]
```
This function first checks if n is less than or equal to 3, in which case it returns the corresponding value from the list `[0, 0, 2, 0]`. If n is greater than 3, it initializes a list `fib4` with the first four values of the sequence and then uses a loop to compute the remaining values of the sequence. The function returns the nth value of the sequence.

The time complexity of this function is O(n) because it needs to compute the values of the sequence up to the nth value. The space complexity is also O(n) because it needs to store the values of the sequence in the list `fib4`. However, the space complexity can be reduced to O(1) by using a loop to compute the values of the sequence in place, without storing them in a list.

Here is the optimized implementation:
```
def Fib4(n):
    if n <= 3:
        return [0, 0, 2, 0][n-1]
    a, b, c, d = 0, 0, 2, 0
    for i in range(4, n+1):
        a, b, c, d = b, c, d, a+b+c+d
    return d
```
This function uses the same algorithm as the previous implementation, but it computes the values of the sequence in place, without storing them in a list. The time complexity is still O(n), but the space complexity is O(1). This implementation is more efficient than the previous one for large values of n.