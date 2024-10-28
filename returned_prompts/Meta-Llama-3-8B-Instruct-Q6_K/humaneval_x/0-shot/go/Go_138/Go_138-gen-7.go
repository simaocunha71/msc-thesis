```go
package main

import (
    "fmt"
)

func IsEqualToSumEven(n int) bool {
    for i := 2; i <= n; i += 2 {
        for j := 2; j <= n-i; j += 2 {
            if i+j > n {
                break
            }
            for k := 2; k <= n-i-j; k += 2 {
                if i+j+k > n {
                    break
                }
                if l := n - i - j - k; l >= 2 && l%2 == 0 {
                    return true
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
The function `IsEqualToSumEven` checks whether the given number `n` can be written as the sum of exactly 4 positive even numbers.

The function uses a nested loop structure to iterate over all possible combinations of even numbers that sum up to `n`. The outer loop iterates over the first even number, the middle two loops iterate over the second and third even numbers, and the innermost loop checks whether the remaining number is even and less than or equal to `n`.

If a combination is found that sums up to `n`, the function returns `true`. If no combination is found after iterating over all possible combinations, the function returns `false`.

In the `main` function, we test the function with the examples provided. The output is as expected.