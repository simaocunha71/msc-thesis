Here is a simple solution in Go:

```go
func DecimalToBinary(decimal int) string {
    binary := fmt.Sprintf("%b", decimal)
    return "db" + strings.Repeat("0", len(binary)) + binary + strings.Repeat("0", len(binary)) + "db"
}
```

In this solution, we use the `fmt.Sprintf` function to convert the decimal number to a binary string. The `%b` format specifier is used to convert the number to a binary string.

Then we add the extra characters 'db' at the beginning and at the end of the string, and also add leading zeros to the binary string to make it the same length as the binary string without leading zeros. The `strings.Repeat` function is used to repeat the string '0' the same number of times as the length of the binary string.  Finally, we return the resulting string. 