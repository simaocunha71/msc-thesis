Here is the solution in Go:

```go
func Solve(N int) string {
    binary := strconv.FormatInt(int64(N), 2)
    sum := 0

    for _, digit := range binary {
        digitInt, _ := strconv.Atoi(string(digit))
        sum += digitInt
    }

    return strconv.Itoa(sum)
}
```

This code first converts the given integer `N` into a binary string using the `strconv.FormatInt` function. Then it iterates over each digit in the binary string, converts it to an integer, and adds it to the `sum`. Finally, it returns the `sum` as a string.