
    // Write your code here
    return 0
}

```

### Answer:

```go
func GetMaxTriples(n int) int {
    count := 0
    for i := 1; i <= n; i++ {
        for j := i + 1; j <= n; j++ {
            for k := j + 1; k <= n; k++ {
                if (i*i-i+1 + j*j-j+1 + k*k-k+1)%3 == 0 {
                    count++
                }
            }
        }
    }
    return count
}
```
This solution uses three nested loops to generate all possible triples (i, j, k). For each triple, it calculates the value of a[i], a[j], and a[k] and checks if their sum is a multiple of 3. If so, it increments the count. Finally, it returns the count.

Note that this solution has a time complexity of O(n^3) because of the three nested loops. If n is large, it may be slow.

Also, please note that the problem statement seems to be a bit misleading. The condition "and a[i] + a[j] + a[k] is a multiple of 3" is not consistent with the given formula for a[i] = i * i - i + 1. For example, for i = 2, j = 3, and k = 4, a[i] + a[j] + a[k] = 2 + 8 + 16 = 26, which is not a multiple of 3.

If you meant to check if the sum of the values of a[i], a[j], and a[k] is a multiple of 3, then the problem is not solvable because the values of a[i], a[j], and a[k] are not known until they are calculated.

If you meant to check if a[i] + a[j] + a[k] is a multiple of 3, then the problem is solvable, but it will be very slow due to the large number of possible triples.

Please clarify the problem statement for a more accurate solution.
