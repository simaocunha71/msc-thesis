```go
package main
import "fmt"
func IsEqualToSumEven(n int) bool {
    for i := 2; i <= n; i += 2 {
        if i > n {
            return false
        }
        for j := 2; j <= n; j += 2 {
            if j > n {
                return false
            }
            for k := 2; k <= n; k += 2 {
                if k > n {
                    return false
                }
                for l := 2; l <= n; l += 2 {
                    if l > n {
                        return false
                    }
                    if i+j+k+l == n {
                        return true
                    }
                }
            }
        }
    }
    return false
}
func main() {
    fmt.Println(IsEqualToSumEven(4)) // false
    fmt.Println(IsEqualToSumEven(6)) // false
    fmt.Println(IsEqualToSumEven(8)) // true
}
```

Explanation:
This problem is a brute-force solution where we iterate over all possible combinations of four even numbers and check if their sum equals the given number `n`. We use four nested loops to generate all combinations of four even numbers. If we find a combination that sums up to `n`, we return `true`. If we finish the loops without finding such a combination, we return `false`.

The time complexity of this solution is O(n^4), which is not efficient for large numbers. A more efficient solution would be to use dynamic programming or recursion to reduce the time complexity. However, this solution is simple and easy to understand.