Here is a simple implementation using Go's built-in `filter` function from the `fmt` package:

```go
package main

import (
    "fmt"
    "reflect"
)

func FilterIntegers(values []interface{}) []int {
    var result []int
    for _, v := range values {
        if reflect.TypeOf(v).Kind() == reflect.Int {
            result = append(result, v.(int))
        }
    }
    return result
}

func main() {
    fmt.Println(FilterIntegers([]interface{}{"a", 3.14, 5}))  // [5]
    fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", {}, []}))  // [1, 2, 3]
}
```

This code iterates over each element in the input slice. It uses the `reflect` package to check if the element is an `int`. If it is, it adds it to the `result` slice. The `result` slice is then returned. 

The `main` function demonstrates how to use this `FilterIntegers` function. It prints the results of filtering the given lists of values. 

Note that this code uses Go's built-in `reflect` package, which is used to inspect the type of a value at runtime. This allows us to check if a value is an `int` without knowing its type at compile time. 

Also note that this code does not check if the `int` value is a NaN (Not a Number) or infinity. If you need to handle these cases, you would need to add additional checks. 

Lastly, this code returns a slice of `int` values. If you need to handle errors or other edge cases, you would need to add additional error handling code. 