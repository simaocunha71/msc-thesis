To filter given list of any values and only keep the integers, you can use the following solution in Go:

```go
package main

import "fmt"

func FilterIntegers(values []interface{}) []int {
    ints := []int{}
    for _, v := range values {
        if _, ok := v.(int); ok {
            ints = append(ints, v.(int))
        }
    }
    return ints
}

func main() {
    fmt.Println(FilterIntegers([]interface{}{"a", 3.14, 5})) // [5]
    fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", map[string]interface{}{}, []interface{}{}})) // [1, 2, 3]
}
```

The `FilterIntegers` function takes a slice of `interface{}` values as input and returns a slice of `int`. It initializes an empty slice `ints` to store the integers. Then, it loops over each value in the input slice using the `range` keyword. Inside the loop, it checks if the value can be converted to an `int` using type assertion (`v.(int)`). If the conversion is successful, it appends the integer value to the `ints` slice using the `append` function. Finally, it returns the `ints` slice containing all the integers.

In the `main` function, two test cases are provided to demonstrate the usage of the `FilterIntegers` function. The first test case filters the integers from the given list `["a", 3.14, 5]` and prints `[5]`. The second test case filters the integers from the given list `[1, 2, 3, "abc", map[string]interface{}{}, []interface{}{}]` and prints `[1, 2, 3]`.

You can run the code and see the output by executing the program.

Note: Type assertion (`v.(int)`) is used to check if a value can be converted to an `int`. If the conversion is successful, the value is of type `int`. Otherwise, a runtime panic occurs.

Let'