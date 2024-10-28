```go
func Tri(n int) []float64 {
    result := make([]float64, n+1)
    if n >= 1 {
        result[0] = 3.0
    }
    if n >= 2 {
        result[1] = 1.0
    }
    if n >= 3 {
        result[2] = 2.0
    }
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


The Tribonacci sequence is defined by the recurrence relation: `Tri(1) = 3`, `Tri(n) = 1 + n / 2` if `n` is even, and `Tri(n) = Tri(n-1) + Tri(n-2) + Tri(n+1)` if `n` is odd. To generate the sequence, we start by initializing a slice of length `n+1` with the first three elements of the sequence. Then, we iterate over the rest of the sequence, using the recurrence relation to calculate each element. If `n` is even, we use the formula `1 + n / 2`. If `n` is odd, we use the formula `Tri(n-1) + Tri(n-2) + Tri(n+1)`. Finally, we return the generated sequence.