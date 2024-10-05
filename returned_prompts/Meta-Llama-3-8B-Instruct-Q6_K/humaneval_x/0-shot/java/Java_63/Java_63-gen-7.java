    public int fibfib(int n) {
        if(n <= 1) {
            return 0;
        }
        if(n == 2) {
            return 1;
        }
        int a = 0, b = 0, c = 1;
        for(int i = 3; i <= n; i++) {
            int temp = a + b + c;
            a = b;
            b = c;
            c = temp;
        }
        return c;
    }
}
```

The code defines a function `fibfib(int n)` that calculates the `n-th` element of the fibfib number sequence. The fibfib sequence is defined as:
- `fibfib(0)` equals 0
- `fibfib(1)` equals 0
- `fibfib(2)` equals 1
- `fibfib(n)` equals `fibfib(n-1)` plus `fibfib(n-2)` plus `fibfib(n-3)`

The function uses a for loop to calculate the `n-th` element. It initializes three variables `a`, `b`, and `c` to 0, 0, and 1, respectively. Then, it iterates from 3 to `n`, updating the values of `a`, `b`, and `c` according to the sequence definition. Finally, it returns the value of `c`, which is the `n-th` element of the fibfib sequence.

The time complexity of this function is O(n), as it needs to iterate `n` times to calculate the `n-th` element. The space complexity is O(1), as it only uses a constant amount of space to store the variables `a`, `b`, and `c`. 