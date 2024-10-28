To filter given list of any values for only integers, we can use the following function:

```go
func FilterIntegers(values []interface{}) []int {
    result := []int{}
    for _, v := range values {
        if _, ok := v.(int); ok {
            result = append(result, v.(int))
        }
    }
    return result
}
```

The function `FilterIntegers` takes a slice of interface values as input and returns a slice of integers. It initializes an empty result slice of integers. Then, it iterates over the input values using the `range` keyword. For each value, it checks if the value can be type-asserted to an integer using the `v.(int)` syntax. If the type assertion is successful, it appends the value to the result slice using the `append` function. Finally, it returns the result slice containing only the integers from the input values.

You can test the function with the following examples:

```go
fmt.Println(FilterIntegers([]interface{}{"a", 3.14, 5})) // [5]
fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", struct{}{}, []interface{}{}})) // [1, 2, 3]
```

The first example will filter out the floating-point number `3.14` and the string `"a"`, leaving only the integer `5` in the result slice. The second example will filter out the non-integer values (string, struct, and interface slice) and keep only the integers `1`, `2`, and `3` in the result slice.

Note that this solution assumes that the input values are of type `interface{}`, which allows for any Go value to be passed in. If you have a specific type constraint for the input values, you can modify the function accordingly.

Additionally, if you have a specific type constraint for the input values, you can modify the function accordingly. For example, if you want to filter only the integers from a slice of `float64` values, you can use the following function:

```go
func FilterIntegers(values []float64) []int {
    result