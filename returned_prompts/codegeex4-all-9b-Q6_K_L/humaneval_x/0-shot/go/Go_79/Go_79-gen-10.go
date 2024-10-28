```go
func DecimalToBinary(decimal int) string {
	return fmt.Sprintf("db%sdb", strconv.FormatInt(int64(decimal), 2))
}
```
