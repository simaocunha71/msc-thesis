```go
func CircularShift(x int, shift int) string {
    shift %= len(strconv.Itoa(x))
    s := strconv.Itoa(x)
    return s[len(s)-shift:] + s[:len(s)-shift]
}
```


Here is the explanation:

1. We convert the integer `x` to a string `s` using `strconv.Itoa(x)`.
2. We calculate the actual shift `shift` by taking the remainder of `shift` divided by the length of the string `s`. This is to handle the case where `shift` is greater than the number of digits.
3. We use slicing to extract the last `shift` characters from the string `s` and concatenate them with the remaining characters to get the circularly shifted string.

For example, if `x` is `12` and `shift` is `1`, we get `s = "12"`, `shift = 1`, and the result is `"21"`. If `shift` is `2`, we get `s = "12"`, `shift = 0`, and the result is still `"12"`. If `shift` is `3`, we get `s = "12"`, `shift = 1`, and the result is still `"21"`. If `shift` is `4`, we get `s = "12"`, `shift = 2`, and the result is still `"12"`. And so on.