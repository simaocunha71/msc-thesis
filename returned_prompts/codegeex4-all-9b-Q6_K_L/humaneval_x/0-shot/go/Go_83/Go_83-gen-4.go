```go
func StartsOneEnds(n int) int {
    if n == 1 {
        return 2
    }
    return 18 * int(math.Pow10(n-2))
}
```

This solution works by considering the total number of n-digit numbers that start with 1 or end with 1. For any n-digit number where n > 1, we can always place a 1 at the beginning or the end. There are 18 such numbers for each n-digit number (since there are 9 choices for the remaining n-1 digits and 2 choices for the first and last digit). Therefore, the total number of such numbers for n digits is 18 * 10^(n-2). For n = 1, there are only 2 such numbers (1 and 10).