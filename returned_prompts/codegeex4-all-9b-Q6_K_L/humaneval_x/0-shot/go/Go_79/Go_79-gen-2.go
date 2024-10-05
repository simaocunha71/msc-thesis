Here is a simple Go function that converts a decimal number to binary and returns the result as a string:

```go
func DecimalToBinary(decimal int) string {
    return "db" + fmt.Sprintf("%b", decimal) + "db"
}
```

This function uses the `fmt.Sprintf` function to convert the decimal number to a binary string. The format specifier `%b` is used to specify that the number should be formatted as a binary string. The extra "db" characters are added at the beginning and end of the string.