To filter the given list of any values only for integers, you can use the following code:

```go
func FilterIntegers(values []interface{}) []int {
    var integers []int
    for _, value := range values {
        switch value := value.(type) {
        case int:
            integers = append(integers, value)
        }
    }
    return integers
}
```

This code defines a function called `FilterIntegers` that takes in a slice of `interface{}` called `values`. It initializes an empty slice of integers called `integers`.

The function then iterates over each value in the `values` slice using the `range` keyword. For each value, it uses a `switch` statement to check its type. If the value is of type `int`, it appends it to the `integers` slice using the `append` function.

Finally, the function returns the `integers` slice, which contains only the integer values from the original `values` slice.

You can call the `FilterIntegers` function with different input values to see the filtered result. For example, `FilterIntegers(['a', 3.14, 5])` will return `[5]`, and `FilterIntegers([1, 2, 3, 'abc', {}, []])` will return `[1, 2, 3]`.

Note that this solution assumes that the input values are of type `interface{}` and may contain any type of values. If you know that the input values are always integers, you can simplify the code by using a type assertion instead of a switch statement:

```go
func FilterIntegers(values []interface{}) []int {
    var integers []int
    for _, value := range values {
        if i, ok := value.(int); ok {
            integers = append(integers, i)
        }
    }
    return integers
}
```

This version of the function checks if each value in the `values` slice can be type-asserted to an `int` using the `value.(int)` syntax. If the type assertion is successful (i.e., the value can be converted to an `int