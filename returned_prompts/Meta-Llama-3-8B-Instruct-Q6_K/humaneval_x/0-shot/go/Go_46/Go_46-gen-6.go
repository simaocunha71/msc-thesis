```
def Fib4(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        fib4_values = [0, 0, 2, 0]
        for i in range(4, n+1):
            fib4_values.append(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4])
        return fib4_values[n]
```
This function first handles the base cases where n is 0, 1, 2, or 3. Then, it initializes a list `fib4_values` to store the values of the sequence. It iterates from 4 to n, calculating each value as the sum of the previous four values, and appends this value to the list. Finally, it returns the nth value from the list. This function has a time complexity of O(n), making it efficient for large values of n. .


