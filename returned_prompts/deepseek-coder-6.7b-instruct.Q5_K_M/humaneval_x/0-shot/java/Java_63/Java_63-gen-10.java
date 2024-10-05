        if (n < 2) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }

        int[] fib = new int[n+1];
        fib[0] = 0;
        fib[1] = 0;
        fib[2] = 1;

        for (int i = 3; i <= n; i++) {
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
        }

        return fib[n];
    }
}


A: Here is the Python solution for the same:
def fibfib(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    fib = [0] * (n+1)
    fib[2] = 1
    for i in range(3, n+1):
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3]
    return fib[n]

print(fibfib(1)) # 0
print(fibfib(5)) # 4
print(fibfib(8)) # 24

In this solution, we use the concept of dynamic programming to store the computed values in fib array and use it to compute the next value in the sequence. This approach reduces the time complexity from exponential to linear.

A: Here is the Javascript solution for the same:
function fibfib(n) {
    if (n < 2) {
        return 0;
    }
    if (n === 2) {
        return 1;
    }
    let fib = new Array(n+1).fill(0);
    fib[2] = 1;
    for (let i = 3; i <= n; i++) {
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
    }
    return fib[n];
}
console.log(fibfib(1)); // 0
console.log(fibfib(5)); // 4
console.log(