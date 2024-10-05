Here's a possible implementation of the `FilterIntegers` function:

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

This function iterates over the given values and checks if each value is an integer. If it is, the integer value is appended to the `result` slice. Finally, the `result` slice is returned.

You can use this function like this:

```go
values := []interface{}{1, 2, 3, "abc", {}, []}
filtered := FilterIntegers(values)
fmt.Println(filtered) // Output: [1 2 3]
```

In this example, the `values` slice contains various types of values, including integers, strings, and empty slices and maps. The `FilterIntegers` function filters out the integers and returns a new slice containing only the integers `[1, 2, 3]`.