```go
package main

import (
    "fmt"
    "reflect"
)

func FilterIntegers(values []interface{}) []int {
    result := make([]int, 0)
    for _, value := range values {
        v := reflect.ValueOf(value)
        if v.Kind() == reflect.Int {
            result = append(result, v.Int())
        }
    }
    return result
}

func main() {
    fmt.Println(FilterIntegers([]interface{}{"a", 3.14, 5})) // [5]
    fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", map[string]int{"a": 1}, []int{1, 2}})) // [1 2 3]
}
```
In this solution, we iterate over the input slice using a range loop. For each value, we use the `reflect` package to get the type of the value. If the type is `reflect.Int`, we append the value to the result slice.

The `reflect.Int()` function returns the underlying `int` value if the value is an `int`, or panics if the value is not an `int`. We use this to safely convert the value to an `int` if it is an `int`.

Note that this solution assumes that the input slice only contains values that can be converted to `int`. If the input slice contains values that cannot be converted to `int`, such as `string`s or `float`s, this solution will not work correctly. You may want to add error handling or type checking to handle these cases.