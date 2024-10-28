```go
func Tri(n int) []float64 {
    result := make([]float64, n+1)
    if n < 1 {
        return result
    }
    result[0] = 1.0
    result[1] = 3.0
    if n == 1 {
        return result[:2]
    }
    result[2] = 1.0 + 2.0/2.0
    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            result[i] = 1.0 + float64(i)/2.0
        } else {
            result[i] = result[i-1] + result[i-2] + result[i-3]
        }
    }
    return result
}
```

Explanation:
The Tribonacci sequence is defined by the recurrence relation given in the problem. We start by initializing a slice `result` of size `n+1` with all elements set to 0.0. Then, we set the first three elements of `result` to 1.0, 3.0, and 1.0 + 2.0/2.0, respectively, as per the definition of the Tribonacci sequence.

Next, we use a for loop to fill in the rest of the elements of `result`. If `i` is even, we set `result[i]` to 1.0 + `float64(i)/2.0`. If `i` is odd, we set `result[i]` to the sum of `result[i-1]`, `result[i-2]`, and `result[i-3]`.

Finally, we return the `result` slice. If `n` is 0, we return an empty slice. If `n` is 1, we return the first two elements of `result`. Otherwise, we return the entire `result` slice.

The time complexity of this solution is O(n), as we need to iterate `n` times to fill in the `result` slice. The space complexity is O(n), as we need to store the `result` slice of size `n+1`.