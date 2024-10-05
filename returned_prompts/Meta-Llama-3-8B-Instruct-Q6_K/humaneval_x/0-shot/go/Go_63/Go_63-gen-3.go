```
func Fibfib(n int) int {
    if n <= 1 {
        return 0
    }
    if n == 2 {
        return 1
    }
    a, b, c := 0, 0, 1
    for i := 3; i <= n; i++ {
        a, b, c = b, c, a+b+c
    }
    return c
}
```

Explanation:

The function `Fibfib` takes an integer `n` as input and returns the `n`-th element of the Fibfib number sequence.

We use a for loop to compute the `n`-th element. We initialize three variables `a`, `b`, and `c` to 0, 0, and 1, which represent the previous three elements of the sequence.

In each iteration of the loop, we update `a`, `b`, and `c` to the next three elements of the sequence. Specifically, `a` becomes `b`, `b` becomes `c`, and `c` becomes `a+b+c`.

After the loop, `c` holds the `n`-th element of the sequence, which is returned by the function.

This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for computing the `n`-th element of the Fibfib number sequence.