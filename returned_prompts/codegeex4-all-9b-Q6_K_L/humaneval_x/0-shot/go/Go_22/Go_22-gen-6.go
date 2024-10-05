```go
func FilterIntegers(values []interface{}) []int {
	var integers []int
	for _, val := range values {
		if i, ok := val.(int); ok {
			integers = append(integers, i)
		}
	}
	return integers
}
```
This function iterates over the given slice of values and checks if each value is of type int. If it is, it appends the value to the slice of integers. Finally, it returns the slice of integers.