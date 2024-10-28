Here is the solution for the problem:

```go
func Tri(n int) []float64 {
    if n == 0 {
        return []float64{}
    }
    if n == 1 {
        return []float64{3.0}
    }
    if n == 2 {
        return []float64{3.0, 2.0}
    }
    result := make([]float64, n+1)
    result[0] = 3.0
    result[1] = 2.0
    result[2] = 3.0
    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            result[i] = 1 + float64(i)/2
        } else {
            result[i] = result[i-1] + result[i-2] + result[i-3]
        }
    }
    return result
}
```

This function returns the first n+1 numbers of the Tribonacci sequence. It uses a loop to calculate each number in the sequence. If the number is even, it's calculated as `1 + n/2`. If the number is odd, it's calculated as the sum of the three preceding numbers in the sequence. The function returns the calculated sequence as a slice of floats. If `n` is 0, 1, or 2, the function returns the correct sequence for these edge cases.