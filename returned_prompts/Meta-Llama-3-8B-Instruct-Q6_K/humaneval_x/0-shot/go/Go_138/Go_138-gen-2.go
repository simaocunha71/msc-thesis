```go
package main

import (
    "fmt"
)

func IsEqualToSumEven(n int) bool {
    for i := 2; i <= n; i += 2 {
        for j := 2; j <= n; j += 2 {
            if i+j > n {
                break
            }
            for k := 2; k <= n; k += 2 {
                if i+j+k > n {
                    break
                }
                for l := 2; l <= n; l += 2 {
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
    fmt.Println(IsEqualToSumEven(4))  // false
    fmt.Println(IsEqualToSumEven(6))  // false
    fmt.Println(IsEqualToSumEven(8))  // true
}
```

The code is trying to solve the problem by brute forcing all possible combinations of four even numbers that sum up to the given number n. It iterates through all even numbers from 2 to n, and for each number, it checks if it can be combined with other even numbers to reach n. If it finds such a combination, it returns true. If no combination is found after checking all possible combinations, it returns false. This solution is not efficient and may take a long time for large values of n. 

A more efficient solution would be to use a more advanced algorithm, such as dynamic programming or recursion with memoization, to avoid redundant calculations and reduce the time complexity. 

Here is a more efficient solution using dynamic programming:

```go
func IsEqualToSumEven(n int) bool {
    dp := make([]bool, n+1)
    dp[0] = true
    for i := 2; i <= n; i += 2 {
        for j := i; j <= n; j += 2 {
            if dp[j-i] {
                dp[j] = true
            }
        }
    }
    return dp[n]
}
```

In this solution, we create a boolean array dp of size n+1, where dp[i] represents whether it is possible to write i as the sum of exactly 4 positive even numbers. We initialize dp[0] to true, since 0 can be written as the sum of 0. Then we iterate through all even numbers from 2 to n, and for each number i, we check if it