```go
package main

import (
    "fmt"
)

func SmallestChange(arr []int) int {
    n := len(arr)
    // Create a new array that contains the length of the longest palindromic subsequence ending at each position.
    dp := make([]int, n)
    dp[0] = 1
    for i := 1; i < n; i++ {
        dp[i] = 1
    }
    for i := 2; i < n; i++ {
        for j := 0; j < i; j++ {
            if arr[i] == arr[n - i - 1] {
                dp[i] = dp[j] + 2
            } else {
                dp[i] = max(dp[i-1], dp[j])
            }
        }
    }
    // The minimum number of changes is n - dp[n-1].
    return n - dp[n-1]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {
    fmt.Println(SmallestChange([]int{1, 2, 3, 5, 4, 7, 9, 6})) // Output: 4
    fmt.Println(SmallestChange([]int{1, 2, 3, 4, 3, 2, 2})) // Output: 1
    fmt.Println(SmallestChange([]int{1, 2, 3, 2, 1})) // Output: 0
}
```
This program uses dynamic programming to solve the problem. It first creates a new array dp where dp\[i] is the length of the longest palindromic subsequence ending at position i. Then it iterates over the array and fills in dp\[i] based on whether arr\[i] is equal to arr\[n-i-1]. If they are equal, it means that the longest palindromic subsequence ending at position i is the longest palindromic subsequence ending at position j plus 2. If they are not equal, it means that the longest palindromic subsequence ending at position i is the maximum of the longest palindromic subsequence ending at position i-1 and the longest palindromic subsequence ending at position j. Finally, it returns n - dp\[n-1], which is the