You can use a type switch to determine if a value is an integer. Here's how you can implement the `FilterIntegers` function:

```go
func FilterIntegers(values []interface{}) []int {
    var result []int
    for _, value := range values {
        switch v := value.(type) {
        case int:
            result = append(result, v)
        }
    }
    return result
}
```

In this function, we iterate over the `values` slice using a `for` loop. Inside the loop, we use a type switch to check the type of each value. If the value is an integer (`int`), we append it to the `result` slice. Finally, we return the `result` slice containing only the integers.

You can test the function with the examples you provided:

```go
func main() {
    fmt.Println(FilterIntegers([]interface{}{'a', 3.14, 5})) // [5]
    fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", map[string]int{}, []int{}})) // [1, 2, 3]
}
```

This will output:

```
[5]
[1 2 3]
```

As expected, the function filters out all non-integer values and returns a slice containing only the integers.