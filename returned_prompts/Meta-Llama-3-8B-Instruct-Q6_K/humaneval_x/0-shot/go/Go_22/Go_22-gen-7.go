You can use the `fmt.Println` function to print the result of the `FilterIntegers` function. Here's the modified code:

```go
package main

import (
    "fmt"
)

func FilterIntegers(values []interface{}) []int {
    var result []int
    for _, v := range values {
        if x, ok := v.(int); ok {
            result = append(result, x)
        }
    }
    return result
}

func main() {
    fmt.Println(FilterIntegers([]interface{}{'a', 3.14, 5})) // [5]
    fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", map[string]int{"a": 1}, []int{1, 2, 3}})) // [1 2 3]
}
```

In the `FilterIntegers` function, we iterate over the input slice and check if each value is an integer using a type assertion. If it is an integer, we append it to the result slice. Finally, we return the result slice.

In the `main` function, we test the `FilterIntegers` function with two different input slices and print the results. The first slice contains a string, a float, and an integer, and the second slice contains integers, a string, a map, and a slice of integers. The function correctly filters out the non-integer values and returns the result.