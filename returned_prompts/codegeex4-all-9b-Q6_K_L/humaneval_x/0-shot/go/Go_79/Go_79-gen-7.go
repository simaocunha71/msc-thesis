Here is a simple way to convert a decimal number to binary in Go:

```go
func DecimalToBinary(decimal int) string {
	return fmt.Sprintf("db%bdb", decimal)
}
```

In this code, the `%b` verb in `fmt.Sprintf` is used to format the integer as a binary number. The `fmt.Sprintf` function returns a formatted string, which is then returned by the `DecimalToBinary` function.