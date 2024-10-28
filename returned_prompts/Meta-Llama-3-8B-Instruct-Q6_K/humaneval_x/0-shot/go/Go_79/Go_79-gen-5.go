Here is a simple and efficient solution in Go:

```go
func DecimalToBinary(decimal int) string {
    binary := fmt.Sprintf("%b", decimal)
    return "db" + strings.Repeat("0", len(binary)) + binary + strings.Repeat("0", len(binary)) + "db"
}
```

This function uses the `fmt.Sprintf` function to convert the decimal number to a binary string. The `%b` format specifier is used to convert the number to a binary string.

Then, it prepends and appends the "db" characters to the binary string, and repeats the character "0" the same number of times as the length of the binary string.

This function will return a string like "db1111db" or "db100000db" as expected.