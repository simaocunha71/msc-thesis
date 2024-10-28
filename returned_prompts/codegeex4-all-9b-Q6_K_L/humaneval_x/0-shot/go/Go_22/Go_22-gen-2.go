Here is a solution using Go:

```go
func FilterIntegers(values []interface{}) []int {
    var result []int
    for _, v := range values {
        if i, ok := v.(int); ok {
            result = append(result, i)
        }
    }
    return result
}
```

This function iterates over the given list of values and checks if each value is an integer using the type assertion syntax `(v.(int))`. If the assertion is successful, the value is appended to the `result` slice. At the end, the function returns the `result` slice containing only the integers.