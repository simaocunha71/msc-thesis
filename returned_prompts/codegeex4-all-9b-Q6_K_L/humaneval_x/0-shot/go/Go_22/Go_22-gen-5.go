You can use a combination of a for loop and type assertion to filter out the integers from the given list. Here's how you can implement the `FilterIntegers` function in Go:

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

In this implementation, we iterate over each value in the given list using a for loop. For each value, we use type assertion to check if it can be asserted to an `int` type. If it can be, we append it to the `result` slice. Finally, we return the `result` slice containing only the integers from the given list.