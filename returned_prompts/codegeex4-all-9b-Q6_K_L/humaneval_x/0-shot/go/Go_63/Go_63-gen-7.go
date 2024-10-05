The FibFib number sequence can be computed using dynamic programming. We can create a slice to store the FibFib values and use a loop to compute the values up to the n-th element.

Here is the implementation in Go:

```go
func Fibfib(n int) int {
    if n < 3 {
        return 0
    }
    
    fibfib := make([]int, n+1)
    fibfib[0] = 0
    fibfib[1] = 0
    fibfib[2] = 1
    
    for i := 3; i <= n; i++ {
        fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3]
    }
    
    return fibfib[n]
}
```

In this implementation, we first handle the base cases where n is less than 3. Then, we create a slice `fibfib` of size `n+1` to store the FibFib values. We initialize the first three elements of `fibfib` to 0, 0, and 1 respectively. 

Next, we use a loop to compute the FibFib values for the remaining elements. For each element `i` from 3 to `n`, we compute the value by adding the previous three FibFib values: `fibfib[i-1]`, `fibfib[i-2]`, and `fibfib[i-3]`. 

Finally, we return the value of `fibfib[n]`, which is the n-th element of the FibFib number sequence.