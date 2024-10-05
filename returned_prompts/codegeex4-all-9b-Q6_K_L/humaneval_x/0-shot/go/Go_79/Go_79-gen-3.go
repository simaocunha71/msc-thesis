Here is a simple solution in Go:

```go
func DecimalToBinary(decimal int) string {
    return fmt.Sprintf("db%bdb", decimal)
}
```

This function uses the `fmt.Sprintf` function to format the decimal number as a binary string, prefixed and suffixed with "db".

The `%b` verb in the format string tells `Sprintf` to format the integer as a binary string.

I hope this helps! Let me know if you have any questions.