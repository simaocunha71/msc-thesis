You can use the `filter` function from the `go-funk` library, which is a functional programming library for Go. Here's how you can do it:

```go
package main

import (
    "fmt"
    "go-funk"
)

func main() {
    values := []interface{}{"a", 3.14, 5}
    filteredIntegers := funk.Filter(values, func(i interface{}) bool {
        return funk.In(i, []interface{}{int(5)})
    }).([]int)
    fmt.Println(filteredIntegers) // Output: [5]

    values = []interface{}{1, 2, 3, "abc", {}, []}
    filteredIntegers = funk.Filter(values, funk.In[int](int(0))).([]int)
    fmt.Println(filteredIntegers) // Output: [1 2 3]
}
```

If you don't want to use a third-party library, you can also achieve this by using a simple loop:

```go
func FilterIntegers(values []interface{}) []int {
    var result []int
    for _, v := range values {
        if x, ok := v.(int); ok {
            result = append(result, x)
        }
    }
    return result
}
```

This function iterates over the input slice, checks if each element is an integer using a type assertion, and if it is, adds it to the result slice. The `ok` variable is used to check if the type assertion was successful. If it was, the value is added to the result slice; otherwise, the loop continues with the next element. The function returns the result slice.