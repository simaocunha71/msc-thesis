```go
func GetMaxTriples(n int) int {
    var res int
    a := make([]int, n)
    for i := 1; i <= n; i++ {
        a[i-1] = i * i - i + 1
    }
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            for k := j + 1; k < n; k++ {
                if (a[i] + a[j] + a[k])%3 == 0 {
                    res++
                }
            }
        }
    }
    return res
}
```

The function `GetMaxTriples(n int) int` is used to find the number of triples `(a[i], a[j], a[k])` of `a` where `i < j < k`, and `a[i] + a[j] + a[k]` is a multiple of 3. It takes an integer `n` as input and returns an integer.

Here is the explanation of the code:

1. We create an array `a` of length `n` and initialize all values to 0.
2. We calculate the values of `a` based on the given formula `a[i] = i * i - i + 1` for each `i` from 1 to `n`.
3. We initialize a variable `res` to 0, which will store the count of valid triples.
4. We use three nested loops to iterate over all possible triples `(a[i], a[j], a[k])`. The outer loop iterates over `i`, the middle loop iterates over `j`, and the inner loop iterates over `k`.
5. For each triple, we check if `a[i] + a[j] + a[k]` is a multiple of 3 by using the modulo operator `%`. If it is, we increment the count `res`.
6. Finally, we return the count `res`.

The time complexity of this solution is O(n^3), which can be improved by using a hash table to store the values of `a[i]` and their frequencies. The space complexity is O(n), which is the space required to store the array `a`.