```go
func GenerateIntegers(a, b int) []int {
    if a > b {
        a, b = b, a
    }
    res := make([]int, 0)
    for i := a; i <= b; i++ {
        str := strconv.Itoa(i)
        for j := 0; j < len(str); j++ {
            if str[j] - '0' % 2 == 0 {
                res = append(res, i)
                break
            }
        }
    }
    return res
}
```

Explanation:
1. First, we check if `a` is greater than `b`. If so, we swap them to ensure `a` is always the smaller number.
2. We create a slice `res` to store the even digits.
3. We loop through each number from `a` to `b` (inclusive) and convert each number to a string using `strconv.Itoa`.
4. We loop through each character in the string and check if the character is an even digit by subtracting the ASCII value of '0' from the character and taking the remainder when divided by 2. If the remainder is 0, it means the digit is even.
5. If the digit is even, we append the original number to the `res` slice and break out of the inner loop.
6. Finally, we return the `res` slice.

Note: The problem statement is a bit unclear, but based on the examples provided, it seems that the function should return the even digits between `a` and `b`, inclusive. If `a` is greater than `b`, the function should still return the even digits in the range from `a` to `b`. If there are no even digits in the range, the function should return an empty slice.