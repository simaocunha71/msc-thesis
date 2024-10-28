Here is a Python solution:

```Python
def fib4(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fib4_values = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib4_values.append(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4])

    return fib4_values[n]
```

This function first handles the base cases for n <= 3, then initializes a list to store the values of the fib4 sequence. It calculates each value in the sequence by adding the previous four values, and returns the nth value. 

This function has a time complexity of O(n) and a space complexity of O(n), as it needs to store all the previous values in the sequence. 

For larger values of n, a more efficient solution would be to use a matrix exponentiation to calculate the nth value in O(log n) time, but this solution is simpler and easier to understand. 

You can test this function with the provided test cases:

```Python
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```


This solution is in Python, but it can be easily translated to other languages like Java, C++, etc.  The logic remains the same.  For example, here is the equivalent Java solution:

```Java
public class Main {
    public static int fib4(int n) {
        if (n <= 1) {
            return 0;
        } else if (n == 2) {
            return 2;
        } else if (n == 3) {
            return 0;
        }

        int[] fib4_values = new int[n+1];
        fib4_values[0] = 0;
        fib4_values[1] = 0;
        fib4_values[2] = 2;
        fib4_values[3] = 0;
        for (int i = 4; i <= n; i++) {
            fib4_values[i] = fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3]