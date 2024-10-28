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
            result[i] = 1.0 + float64(i)/2
        } else {
            result[i] = result[i-1] + result[i-2] + result[i-3]
        }
    }
    return result
}
```


Explanation:
The Tribonacci sequence is a sequence of numbers where each number is the sum of the previous three numbers. We can use dynamic programming to calculate the sequence.

We start by initializing an array `result` of size `n+1` with the first three numbers of the sequence: 1, 3, and 2. We then iterate from 3 to `n`, and for each `i`, we check if `i` is even or odd.

If `i` is even, we calculate the `i`th number as `1 + i/2`. If `i` is odd, we calculate the `i`th number as the sum of the previous three numbers: `result[i-1] + result[i-2] + result[i-3]`.

Finally, we return the `result` array. The time complexity is O(n) and the space complexity is O(n).