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
    result[0] = 1.0
    result[1] = 3.0
    result[2] = 2.0
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


The Tribonacci sequence is a sequence in which each term is the sum of the previous three terms. The sequence starts with 1, 3, and 2, and each subsequent term is the sum of the previous three.

The function `Tri(n int)` returns the first `n+1` numbers of the Tribonacci sequence. It uses a loop to calculate each term in the sequence. If `n` is even, the term is calculated as `1 + n/2`. If `n` is odd, the term is calculated as the sum of the previous three terms.

The function also handles the base cases where `n` is 0, 1, or 2. In these cases, the function returns the correct sequence.

The function uses a slice to store the sequence, and it returns the slice at the end. The slice is initialized with the first three terms of the sequence, and then each subsequent term is calculated and added to the slice.

The time complexity of this function is O(n), where n is the input number. The space complexity is also O(n), as the function uses a slice to store the sequence.