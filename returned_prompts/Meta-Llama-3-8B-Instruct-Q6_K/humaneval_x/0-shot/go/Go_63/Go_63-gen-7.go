```
func Fibfib(n int) int {
    if n <= 1 {
        return 0
    } else if n == 2 {
        return 1
    } else {
        a, b, c := 0, 0, 1
        for i := 3; i <= n; i++ {
            a, b, c = b, c, a+b+c
        }
        return c
    }
}
```



### Explanation:
The `Fibfib` function computes the `n-th` element of the Fibfib number sequence. It uses a simple iterative approach with three variables `a`, `b`, and `c` to keep track of the last three elements of the sequence. The base cases are handled separately to avoid unnecessary computations.

Here's a breakdown of the function:

1. If `n` is less than or equal to 1, the function returns 0, as per the definition of the Fibfib sequence.
2. If `n` is 2, the function returns 1, as per the definition of the Fibfib sequence.
3. For `n` greater than 2, the function initializes `a`, `b`, and `c` to 0, 0, and 1, respectively. These variables represent the last three elements of the sequence.
4. The function then enters a loop that runs from `i = 3` to `n`. In each iteration, it updates `a`, `b`, and `c` to `b`, `c`, and `a+b+c`, respectively. This effectively shifts the sequence by one position and adds the new element to the end.
5. After the loop, the function returns the value of `c`, which is the `n-th` element of the Fibfib sequence.

This approach has a time complexity of O(n) and a space complexity of O(1), making it efficient for computing large values of `n`.