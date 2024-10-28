You can use a simple for loop to iterate over the slice and check if each element is an integer. If it is, add it to a new slice. Here is the code:

```go
func FilterIntegers(values []interface{}) []int {
    var result []int
    for _, value := range values {
        if v, ok := value.(int); ok {
            result = append(result, v)
        }
    }
    return result
}
```

This function uses a type assertion (`value.(int)`) to check if the value is an integer. If it is, it adds it to the `result` slice. The `ok` variable is used to check if the type assertion was successful. If it was, then `ok` will be `true`. 

Here's how you can use this function:

```go
package main

import (
	"fmt"
)

func FilterIntegers(values []interface{}) []int {
    var result []int
    for _, value := range values {
        if v, ok := value.(int); ok {
            result = append(result, v)
        }
    }
    return result
}

func main() {
	fmt.Println(FilterIntegers([]interface{}{'a', 3.14, 5}))  // [5]
	fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", {}, []}))  // [1 2 3]
}
```


This code will print: `[5]` and `[1 2 3]`. 

Remember that the type assertion will panic if the value is not an integer. If you want to avoid this, you can use a type switch:

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

This code will not panic if the value is not an integer. Instead, it will simply skip it. 