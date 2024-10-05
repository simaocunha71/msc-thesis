You can solve this problem by using a loop to generate all n-digit positive integers that start or end with 1, and count the number of such integers.

Here is the solution:

```go
import (
    "math"
)

func StartsOneEnds(n int) int {
    count := 0
    for i := 1; i <= 9; i++ {
        for j := 1; j <= 10 - n; j++ {
            num := int(math.Pow10(n-1)) + i*int(math.Pow10(n-2)) + j
            if num >= 10 && num % 10 == 1 {
                count++
            }
        }
    }
    for i := 1; i <= 9; i++ {
        num := int(math.Pow10(n-1)) + i
        if num % 10 == 1 {
            count++
        }
    }
    return count
}
```

This solution generates all n-digit positive integers that start or end with 1, and counts the number of such integers. The outer loop generates the first digit of the integer, and the inner loop generates the remaining digits. The `math.Pow10` function is used to calculate the powers of 10, and the `int` function is used to convert the result to an integer. The `if` statement checks if the integer starts or ends with 1, and increments the count if it does. The function returns the total count of integers that start or end with 1.