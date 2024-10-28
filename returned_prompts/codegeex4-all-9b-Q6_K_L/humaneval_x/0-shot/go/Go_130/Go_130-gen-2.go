You can solve this problem by using a recursive function to calculate the Tribonacci numbers. Here is the solution in Go:

```go
func Tri(n int) []float64 {
    if n == 0 {
        return []float64{3}
    }
    if n == 1 {
        return []float64{1, 3}
    }
    if n == 2 {
        return []float64{1, 3, 2}
    }
    result := make([]float64, n+1)
    result[0], result[1], result[2] = 1, 3, 2
    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            result[i] = 1 + float64(i)/2
        } else {
            result[i] = result[i-1] + result[i-2] + result[i+1]
        }
    }
    return result
}
```

This solution first handles the special cases where n is 0, 1, or 2. Then it creates a slice of length n+1 to store the Tribonacci numbers. It initializes the first three elements of the slice and then uses a loop to calculate the remaining elements. The loop checks if the index is even or odd and calculates the corresponding Tribonacci number accordingly. Finally, it returns the resulting slice.