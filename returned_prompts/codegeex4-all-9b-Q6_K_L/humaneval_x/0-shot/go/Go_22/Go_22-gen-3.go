You can use the built-in `reflect` package to check the type of each value in the list. Here's an example implementation:

```go
package main

import (
	"fmt"
	"reflect"
)

func FilterIntegers(values []interface{}) []int {
	var result []int

	for _, value := range values {
		if reflect.TypeOf(value).Kind() == reflect.Int {
			result = append(result, value.(int))
		}
	}

	return result
}

func main() {
	fmt.Println(FilterIntegers([]interface{}{'a', 3.14, 5})) // [5]
	fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", map[string]interface{}{}, []interface{}{}})) // [1, 2, 3]
}
```

In this implementation, we iterate over each value in the `values` slice. We use the `reflect.TypeOf()` function to get the type of each value, and then check if the kind of the type is `reflect.Int`. If it is, we append the value to the `result` slice.

Note that we need to use a type assertion (`value.(int)`) to convert the `interface{}` type to an `int` type before appending it to the `result` slice.