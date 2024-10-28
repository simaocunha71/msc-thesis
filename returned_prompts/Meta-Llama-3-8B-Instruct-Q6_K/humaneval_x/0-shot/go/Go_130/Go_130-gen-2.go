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
    result := []float64{3.0, 2.0}
    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            result = append(result, 1.0+float64(i)/2.0)
        } else {
            a, b := result[i-1], result[i-2]
            result = append(result, a+b+float64(i-1))
        }
    }
    return result
}
```

Explanation:

The Tribonacci sequence is defined by a set of recurrence relations. In this problem, we need to generate the first n+1 numbers of the Tribonacci sequence.

We first handle the base cases: when n is 0, the result is an empty list; when n is 1, the result is [3.0]; when n is 2, the result is [3.0, 2.0].

Then we use a for loop to generate the remaining numbers in the sequence. If the current number is even, we calculate it as 1.0 + (i/2.0); otherwise, we calculate it as the sum of the last two numbers in the sequence and the number before the last one.

Finally, we return the result list. The time complexity of this solution is O(n), and the space complexity is also O(n), as we need to store the result list.