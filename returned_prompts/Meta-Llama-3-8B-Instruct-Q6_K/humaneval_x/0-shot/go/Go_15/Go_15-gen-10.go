```go
func StringSequence(n int) string {
    result := ""
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return strings.TrimSpace(result)
}
```


The `StringSequence` function generates a string containing space-delimited numbers starting from 0 up to `n` inclusive. It does this by iterating over the range from 0 to `n` (inclusive) and converting each integer to a string using `strconv.Itoa`. The strings are concatenated with a space in between using the `+=` operator. The `strings.TrimSpace` function is used to remove any trailing spaces from the result before returning it.

For example, `StringSequence(5)` would return the string `"0 1 2 3 4 5"`. If `n` is 0, the function will return the string `"0"`. If `n` is negative, the function will return an empty string. If `n` is a large positive integer, the function will return a string with many space-delimited numbers.