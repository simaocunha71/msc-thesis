```go
func Tri(n int) []float64 {
    if n <= 0 {
        return []float64{}
    }
    result := make([]float64, n+1)
    if n == 1 {
        result[0] = 3.0
        return result
    }
    result[0] = 3.0
    result[1] = 1.0
    for i := 2; i <= n; i++ {
        if i%2 == 0 {
            result[i] = 1.0 + float64(i)/2
        } else {
            result[i] = result[i-1] + result[i-2] + result[i-3]
        }
    }
    return result
}
```


The solution is straightforward. It starts by initializing a result slice with a size of n+1. The base cases are handled by setting the first two elements of the result slice. Then, it iterates over the remaining elements of the result slice, using the recurrence relation to calculate each element. If the index is even, it calculates the element as 1 + n/2. If the index is odd, it calculates the element as the sum of the previous three elements. Finally, it returns the result slice.