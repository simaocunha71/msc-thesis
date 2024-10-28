```go
func DecimalToBinary(decimal int) string {
	return fmt.Sprintf("db%sdb", fmt.Sprintf("%b", decimal))
}
```