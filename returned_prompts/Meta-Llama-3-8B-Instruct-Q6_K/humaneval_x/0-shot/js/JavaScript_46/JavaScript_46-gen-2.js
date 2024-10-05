Here is a Python solution for the problem:

```Python
def fib4(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    else:
        fib4_values = [0, 0, 2]
        for i in range(3, n+1):
            fib4_values.append(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4])
        return fib4_values[n]
```

Here is a JavaScript solution for the problem:

```JavaScript
function fib4(n) {
    if (n <= 1) {
        return 0;
    } else if (n === 2) {
        return 2;
    } else {
        let fib4_values = [0, 0, 2];
        for (let i = 3; i <= n; i++) {
            fib4_values.push(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4]);
        }
        return fib4_values[n];
    }
}
```
The idea behind this solution is to use a loop to compute the first `n` elements of the fib4 sequence. We start with the base cases `fib4(0)`, `fib4(1)` and `fib4(2)`, and then compute the rest of the sequence by iterating from 3 to `n`. At each step, we add the last 4 elements of the sequence to get the next one. The function returns the `n`-th element of the sequence.

This solution has a time complexity of O(n) and a space complexity of O(n), because we need to store the first `n` elements of the sequence. This is the most efficient solution, because it avoids the overhead of function calls and uses a simple loop to compute the sequence. 