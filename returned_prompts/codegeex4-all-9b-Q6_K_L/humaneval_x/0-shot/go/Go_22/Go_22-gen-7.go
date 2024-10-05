You can use the built-in type assertion to check if a value is an integer. Here is the code:

```go
func FilterIntegers(values []interface{}) []int {
    var result []int
    for _, value := range values {
        if intValue, ok := value.(int); ok {
            result = append(result, intValue)
        }
    }
    return result
}
```

This function iterates over the given slice of interface{} values. If a value can be asserted as an int, it is appended to the result slice. Finally, the result slice is returned.