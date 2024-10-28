Here is a solution in Go:

```go
func DecimalToBinary(decimal int) string {
	return fmt.Sprintf("db%bdb", decimal)
}
```

This function uses the `fmt.Sprintf` function to format the decimal number into a binary string. The `%b` verb is used to format an integer as a binary string.

For example, `DecimalToBinary(15)` will return the string "db1111db" and `DecimalToBinary(32)` will return the string "db100000db".