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


The function `Fibfib` calculates the nth element of the Fibfib sequence. It uses a for loop to iterate from 3 to n, and at each iteration, it updates the values of `a`, `b`, and `c` according to the definition of the Fibfib sequence.

The base cases are handled separately: if `n` is 0 or 1, the function returns 0, and if `n` is 2, the function returns 1.

The time complexity of this function is O(n), which is efficient for calculating the nth element of the Fibfib sequence. The space complexity is O(1), as it only uses a constant amount of space to store the values of `a`, `b`, and `c`.