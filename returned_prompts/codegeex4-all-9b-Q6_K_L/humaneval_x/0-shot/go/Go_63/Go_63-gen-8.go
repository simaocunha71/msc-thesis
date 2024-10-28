The FibFib number sequence is a sequence similar to the Fibbonacci sequence, but with an additional term in the sum. The FibFib sequence is defined as follows:

Fibfib(0) == 0
Fibfib(1) == 0
Fibfib(2) == 1
Fibfib(n) == Fibfib(n-1) + Fibfib(n-2) + Fibfib(n-3)

To efficiently compute the n-th element of the Fibfib number sequence, we can use a recursive function. However, recursion can be inefficient for large values of n because it involves a lot of redundant calculations. To optimize the computation, we can use memoization, which is a technique that stores the results of expensive function calls and returns the cached result when the same inputs occur again.

Here's the implementation of the Fibfib function using memoization:

```go
func Fibfib(n int) int {
    memo := make(map[int]int)
    return fibfibMemo(n, memo)
}

func fibfibMemo(n int, memo map[int]int) int {
    if n < 2 {
        return 0
    }
    if n == 2 {
        return 1
    }
    if val, ok := memo[n]; ok {
        return val
    }
    result := fibfibMemo(n-1, memo) + fibfibMemo(n-2, memo) + fibfibMemo(n-3, memo)
    memo[n] = result
    return result
}
```

In this implementation, we define a helper function `fibfibMemo` that takes an additional argument `memo`, which is a map used to store the results of previously computed Fibfib values. We first check if the result for the given n is already in the memo map. If it is, we return the cached result. Otherwise, we compute the result recursively and store it in the memo map before returning it.

By using memoization, we can avoid redundant calculations and efficiently compute the n-th element of the Fibfib number sequence for large values of n.